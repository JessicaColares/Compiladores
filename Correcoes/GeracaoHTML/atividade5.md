## Trabalho 05 - Geração de páginas HTML

Baseado nas aulas e slides sobre como gerar páginas web, altere o parser para, além de verificar se a entrada está de acordo com a gramática, que também inclua **três** funcionalidades descritas a seguir.

(1) um menu de seleção simples. A entrada fornecerá o identificador do menu, o rótulo do menu, os identificadores e rótulos de cada opção do menu. Veja o exemplo abaixo.

```
<label for="cars">Choose a car:</label>
<select name="cars" id="cars">
  <option value="volvo">Volvo</option>
  <option value="saab">Saab</option>
  <option value="mercedes">Mercedes</option>
  <option value="audi">Audi</option>
</select>
```

(2) um botão que receba da entrada o rótulo do botão e ação quando clicar deve ser necessariamente um alerta. Para tanto, a entrada também fornecerá o que será mostrado no alerta. Veja o exemplo abaixo.

```
<button type="button" onclick="alert('Hello world!')">Click Me!</button>
```

(3) uma tabela que inclua uma linha de cabeçalho (header) + linhas da tabela + legenda (caption). O exemplo abaixo mostra uma definição de uma tabela em HTML com todos esses elementos.

```
<table>
  <caption>Monthly savings</caption>
  <tr>
    <th>Month</th>
    <th>Savings</th>
  </tr>
  <tr>
    <td>January</td>
    <td>$100</td>
  </tr>
  <tr>
    <td>February</td>
    <td>$50</td>
  </tr>
</table>
```

Altere a gramática dos slides para incluir as **três** funcionalidades acima da seguinte forma:

```
qMenu: 'MENU' str_ str_ menuOpcoes;
menuOpcoes: '(' menuOpcao (',' menuOpcao)* ')';
menuOpcao: str_ ':' str_;
```

```
qBotao: 'BOTAO' str_ str_;
```

```
qTabela: 'TABELA' str_ linhaCabecalho linhaDados;
linhaCabecalho: '(' str_ (',' str_)* ')';
linhaDados: '(' linha (',' linha)* ')';
linha: '(' str_ (',' str_)* ')';
```

No site [https://www.w3schools.com/tags/tag\_select.asp](https://www.w3schools.com/tags/tag_select.asp) é possível testar as tuas próprias tags HTML.

Implementar um analisador léxico + sintático + semântico que, a partir da gramática, gere uma página HTML usando VISITOR ou LISTENER.

Gere uma entrada e experimente para verificar se o gerador de página HTML está funcionando.

Entregue quatro arquivos: a gramática, o visitor (ou listener), o programa principal e a entrada de teste. Comprima os quatro arquivos usando o "zip" (tem que ser zip). Coloque o seu nome como nome do arquivo zipado.

Para facilitar, segue em anexo a gramática e o visitor que mostrei em sala de aula.

### html.g

```
grammar Html;

root: questao+;

questao: (qTexto | qRadioBox | qCheckBox);

qTexto: 'TEXTO' NUMERO NUMERO str_;

qRadioBox: 'ESCOLHAUMA' str_ opcoes;

qCheckBox: 'ESCOLHAVARIAS' str_ opcoes;

opcoes: '(' str_ (',' str_)* ')';

str_: STRING;

// TOKENS:
NUMERO: [0-9]+;
STRING: '"' (~["])* '"';
IGNORE: [ \n\r\t] -> skip; 
COMMENT: '#' ~[\r\n]* -> skip;
```

### visitor.py

```
from HtmlParser import HtmlParser
from HtmlVisitor import HtmlVisitor

class HtmlOutput():
  
    def __init__(self):
        self.conteudo = ""
        self.count = 0

    def HtmlOutput(self):
        self.count = 0
        self.conteudo = "<html>\n"
        self.conteudo += "<head><title>Formulario</title></head>\n"
        self.conteudo += "<body>\n"
        self.conteudo += "<form>\n"

    def addText(self, cols, rows, s):
        self.conteudo += s + "<br>\n"
        self.conteudo += "<textarea name='Q" + str(self.count) + "' cols='" + str(cols) + "' rows='" + str(rows) + "'></textarea><br>\n"
        self.conteudo += "<br>\n\n"
        self.count += 1
  
    def addRadio(self, s, options):
        self.conteudo += s + "<br>\n"
        for val in options:
            self.conteudo += "<input type='radio' name='Q" + str(self.count) + "' "
            self.conteudo += "value='" + val + "'>" + val + "<br>\n"
      
        self.conteudo += "<br>\n\n"
        self.count+=1
  
    def addCheckBox(self, s , options):
        self.conteudo += s + "<br>\n"
      
        for val in options: 
            self.conteudo += "<input type='checkbox' name='Q" + str(self.count) + "' "
            self.conteudo += "value='" + val + "'>" + val + "<br>\n"
            self.count+=1
      
        self.conteudo += "<br>\n\n"

    def close(self):
        self.conteudo += "</form>\n"
        self.conteudo += "</body>\n"
        self.conteudo += "</html>\n"
        print(self.conteudo)


class Visitor(HtmlVisitor):

    def __init__(self):
        self.html = HtmlOutput()

    def visitRoot(self, ctx):
        l = list(ctx.getChildren())
        for questao in l:
            self.visit(questao)

        self.html.close()
     
    def visitQTexto(self, ctx):
        l = list(ctx.getChildren())
      
        if(len(l) == 4):
            cols = l[1].getText()
            rows = l[2].getText()
            string = self.visit(l[3])
          
            self.html.addText(cols, rows, string)

    def visitQRadioBox(self, ctx):
        l = list(ctx.getChildren())
      
        if(len(l) == 3):
            string = self.visit(l[1])
            opcoes = self.visit(l[2])
            self.html.addRadio(string, opcoes)
  
    def visitQCheckBox(self, ctx: HtmlParser.QCheckBoxContext):
        l = list(ctx.getChildren())
      
        if(len(l) == 3):
            string = self.visit(l[1])
            opcoes = self.visit(l[2])
            self.html.addCheckBox(string, opcoes)

    def visitOpcoes(self, ctx):
        l = list(ctx.getChildren())
        qtdStr = (len(l) - 2) // 2 # retirando os '()' e ','
        opcoes = []
      
        for i in range(qtdStr + 1):
            opcoes.append(self.visit(ctx.str_(i)))
      
        return opcoes
 
    def visitStr_(self, ctx):
        l = list(ctx.getChildren())
        string = l[0].getText().replace('"','')
        return string
```
