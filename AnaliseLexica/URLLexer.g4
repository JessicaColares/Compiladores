lexer grammar URLLexer;

// Compiladores - Atividade Analisador Lexico
// Nome: Jessica de Figueredo Colares
// Matricula: 22060036

// Palavras-chave para protocolos (aceitando ambas as formas)
HTTP: ('http');
HTTPS: ('https');
FTP: ('ftp');

// Componentes da URL
PROTOCOL_SEP: '://';
DOMAIN: [a-zA-Z0-9]+([.-][a-zA-Z0-9]+)*;
PORT: ':' [0-9]+;
PATH: '/' (~[?#] | '\\' [?#])*;
QUERY: '?' ( ~[#&] | '&' )+;
FRAGMENT: '#' ~[\r\n]+;

// Ignorar espaços em branco
WS: [ \t\r\n]+ -> skip;