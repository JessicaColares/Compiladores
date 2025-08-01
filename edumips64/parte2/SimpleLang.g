grammar SimpleLang;

program: (global_declaration | function)* EOF;

global_declaration: type var_list ';';

function: type ID '(' params? ')' block;

params: 'void' | param (',' param)*;
param: type ID;

block: '{' (declaration | statement)* '}';

declaration: type var_list ';';

var_list: ID ('=' expression)? (',' ID ('=' expression)?)*;

statement
    : exprStmt
    | returnStmt
    | ifStmt
    | whileStmt
    | ';'                          // instrução vazia
    ;

exprStmt: expression ';';
returnStmt: 'return' expression? ';';

ifStmt: 'if' '(' expression ')' block ('else' block)?;
whileStmt: 'while' '(' expression ')' block;

expression
    : expression op=('*' | '/' | '%') expression                        # mulDivExpr
    | expression op=('+' | '-') expression                              # addSubExpr
    | expression op=('<' | '<=' | '>' | '>=' | '==' | '!=') expression  # relExpr
    | ID '=' expression                                                 # assignExpr
    | ID op=('*=' | '/=' | '+=' | '-=') expression                      # compoundAssignExpr
    | '++' ID                                                           # preIncExpr
    | '--' ID                                                           # preDecExpr
    | 'printf' '(' STRING ',' (ID | INT | CHAR) ')'                     # printfExpr
    | ID                                                                # varExpr
    | INT                                                               # intExpr
    | CHAR                                                              # charExpr
    | STRING                                                            # stringExpr
    | ID '(' argList? ')'                                               # callExpr
    | '(' expression ')'                                                # parensExpr
    ;

argList: (expression | STRING) (',' (expression | STRING))*;

// Tipos suportados
type: 'int' | 'char' | 'void';

// Tokens
ID: [a-zA-Z_][a-zA-Z0-9_]*;
INT: [0-9]+;
CHAR: '\'' . '\'';
STRING: '"' (~["\\] | '\\' .)* '"';
WS: [ \t\r\n]+ -> skip;
COMMENT: '//' ~[\r\n]* -> skip;
