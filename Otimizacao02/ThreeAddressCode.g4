grammar ThreeAddressCode;

program: (line? EOL)*;

line: assignment | return_stmt | label | goto | EOL;

assignment: ID '=' expr;
return_stmt: 'return' expr;
label: ID ':';
goto: 'goto' ID;

expr: 
    '(' expr ')'                  # parenExpr 
    | expr op=('*'|'/') expr      # binaryExpr
    | expr op=('+'|'-') expr      # binaryExpr
    | ID                          # id
    | INT                         # int
    ;

ID: [a-zA-Z_][a-zA-Z0-9_]*;
INT: [0-9]+;
EOL: '\r'?'\n';
WS: [ \t]+ -> skip;