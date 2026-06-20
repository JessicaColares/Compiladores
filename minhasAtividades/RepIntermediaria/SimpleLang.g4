grammar SimpleLang;

prog: (function|statement)+ ;

function: 'int' ID '(' ')' block ;

statement: ifStatement
         | whileStatement
         | assignment ';'
         | declaration ';'
         | returnStatement ';'
         | ';';

ifStatement: 'if' '(' expression ')' block ('else' block)? ;

whileStatement: 'while' '(' expression ')' block ;

declaration: 'int' ID ('=' expression)? ;

assignment: ID '=' expression ;

returnStatement: 'return' expression ;

block: '{' statement* '}' ;

expression: logicalOr ;

logicalOr: logicalAnd ('||' logicalAnd)* ;

logicalAnd: equality ('&&' equality)* ;

equality: relational (('=='|'!=') relational)* ;

relational: additive (('<'|'>'|'<='|'>=') additive)* ;

additive: multiplicative (('+'|'-') multiplicative)* ;

multiplicative: unary (('*'|'/') unary)* ;

unary: ('!'|'-') unary | primary ;

primary: '(' expression ')'
       | ID
       | INT
       ;

ID  : [a-zA-Z_][a-zA-Z0-9_]* ;
INT : [0-9]+ ;
WS  : [ \t\r\n]+ -> skip ;
COMMENT: '/*' .*? '*/' -> skip;
LINE_COMMENT: '//' ~[\r\n]* -> skip;