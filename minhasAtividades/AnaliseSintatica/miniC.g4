grammar miniC;

program
    : definition+
    ;

definition
    : data_definition
    | function_definition
    ;

data_definition
    : INT declarator (',' declarator)* ';'
    ;

declarator
    : IDENTIFIER
    ;

function_definition
    : (INT)? function_header function_body
    ;

function_header
    : declarator parameter_list
    ;

parameter_list
    : '(' (parameter_declaration)? ')'
    ;

parameter_declaration
    : INT declarator (',' INT declarator)*
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
    | primary
    ;

primary
    : IDENTIFIER
    | CONSTANT_INT
    | '(' expression ')'
    | IDENTIFIER '(' (argument_list)? ')'
    ;

argument_list
    : binary (',' binary)*
    ;

// Palavras reservadas
IF: 'if';
ELSE: 'else';
WHILE: 'while';
BREAK: 'break';
CONTINUE: 'continue';
RETURN: 'return';
INT: 'int';

// Tokens
IDENTIFIER: [a-zA-Z_][a-zA-Z0-9_]*;
CONSTANT_INT: [0-9]+;

// Ignorar espaços e comentários
WS: [ \t\r\n]+ -> skip;
COMMENT: '/*' .*? '*/' -> skip;
LINE_COMMENT: '//' ~[\r\n]* -> skip;