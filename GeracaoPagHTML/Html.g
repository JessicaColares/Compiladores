grammar Html;

root: questao+;

questao: (qTexto | qRadioBox | qCheckBox | qMenu | qBotao | qTabela);

qTexto: 'TEXTO' NUMERO NUMERO str_;
qRadioBox: 'ESCOLHAUMA' str_ opcoes;
qCheckBox: 'ESCOLHAVARIAS' str_ opcoes;
qMenu: 'MENU' str_ str_ opcoesValores;
qBotao: 'BOTAO' str_ str_;
qTabela: 'TABELA' str_ cabecalho linha+;

opcoes: '(' str_ (',' str_)* ')';
opcoesValores: '(' parStrStr (',' parStrStr)* ')';
cabecalho: '(' str_ (',' str_)* ')';
linha: '(' str_ (',' str_)* ')';
parStrStr: str_ str_;

str_: STRING;

// TOKENS:
NUMERO: [0-9]+;
STRING: '"' (~["])* '"';
IGNORE: [ \n\r\t] -> skip; 
COMMENT: '#' ~[\r\n]* -> skip;