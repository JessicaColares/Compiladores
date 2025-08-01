Trabalho 05 - Geração de páginas HTML
Este trabalho pode ser feito em duplas.

Baseado nas aulas e slides sobre como gerar páginas web, altere o parser para, além de verificar se a entrada está de acordo com a gramática, que também inclua três funcionalidades descritas a seguir.

(1) um menu de seleção simples. A entrada fornecerá o identificador do menu, o rótulo do menu, os identificadores e rótulos de cada opção do menu. Veja o exemplo abaixo.

<label for="cars">Choose a car:</label>
<select name="cars" id="cars">
  <option value="volvo">Volvo</option>
  <option value="saab">Saab</option>
  <option value="mercedes">Mercedes</option>
  <option value="audi">Audi</option>
</select>
(2) um botão que receba da entrada o rótulo do botão e ação quando clicar deve ser necessariamente um alerta. Para tanto, a entrada também fornecerá o que será mostrado no alerta. Veja o exemplo abaixo.

<button type="button" onclick="alert('Hello world!')">Click Me!</button>
(3) uma tabela que inclua uma linha de cabeçalho (header) + linhas da tabela + legenda (caption). O exemplo abaixo mostra uma definição de uma tabela em HTML com todos esses elementos.

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
Altere a gramática vista em sala de aula para incluir as três funcionaldades acima. Para tanto, você deve incluir as palavras-chave BOTAO, MENU e TABELA na nova gramática. Fique a vontade para alterar a gramática e inclusão dos parâmetros necessários da forma como você quiser.

Sugiro implementar usando VISITOR, mas não me importo se você implementar usando LISTENER.

No site https://www.w3schools.com/tags/tag_select.asp é possível testar as tuas próprias tags HTML.

Entregue três arquivos: a gramática, o visitor (ou listener) e o programa principal. Comprima os três arquivos usando o "zip". Coloque os nomes da dupla como nome do arquivo zipado.

Para facilitar, segue em anexo a gramática e o visitor que mostrei em sala de aula.


para rodar o programa
python main.py > output.html