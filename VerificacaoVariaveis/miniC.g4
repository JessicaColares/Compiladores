grammar miniC;

program
    : definition+
    ;

definition
    : data_definition
    | function_definition
    ;

data_definition
    : type declarator (',' declarator)* ';'
    | type declarator '=' expression ';'
    ;

type
    : INT
    | CHAR
    ;

declarator
    : IDENTIFIER
    | IDENTIFIER '=' expression
    ;
function_definition
    : type? function_header function_body
    ;

function_header
    : IDENTIFIER parameter_list
    ;

parameter_list
    : '(' (parameter_declaration (',' parameter_declaration)*)? ')'
    ;

parameter_declaration
    : type declarator
    ;

function_body
    : '{' (data_definition)* (statement)* '}'
    ;

block
    : '{' (statement)* '}'
    ;

statement
    : expression ';'
    | IF '(' expression ')' statement (ELSE statement)?
    | WHILE '(' expression ')' statement
    | BREAK ';'
    | CONTINUE ';'
    | RETURN (expression)? ';'
    | block
    | ';'
    ;

expression
    : binary
    ;

binary
    : IDENTIFIER '=' binary
    | IDENTIFIER '+=' binary
    | IDENTIFIER '-=' binary
    | IDENTIFIER '*=' binary
    | IDENTIFIER '/=' binary
    | IDENTIFIER '%=' binary
    | binary '==' binary
    | binary '!=' binary
    | binary '<' binary
    | binary '<=' binary
    | binary '>=' binary
    | binary '>' binary
    | binary '+' binary
    | binary '-' binary
    | binary '*' binary
    | binary '/' binary
    | binary '%' binary
    | unary
    ;

unary
    : '++' IDENTIFIER
    | '--' IDENTIFIER
    | IDENTIFIER '++'
    | IDENTIFIER '--'
    | primary
    ;

primary
    : IDENTIFIER
    | CONSTANT_INT
    | CONSTANT_CHAR
    | '(' expression ')'
    | IDENTIFIER '(' (argument_list)? ')'
    ;

argument_list
    : expression (',' expression)*
    ;

// Palavras reservadas
IF: 'if';
ELSE: 'else';
WHILE: 'while';
BREAK: 'break';
CONTINUE: 'continue';
RETURN: 'return';
INT: 'int';
CHAR: 'char';

// Tokens
IDENTIFIER: [a-zA-Z_][a-zA-Z0-9_]*;
CONSTANT_INT: [0-9]+;
CONSTANT_CHAR: '\'' . '\'';

// Ignorar espaços e comentários
WS: [ \t\r\n]+ -> skip;
COMMENT: '/*' .*? '*/' -> skip;
LINE_COMMENT: '//' ~[\r\n]* -> skip;