// MiniC.g4
grammar MiniC;

// Starting rule for the parser
program: declaration+ EOF;

declaration
    : functionDefinition
    ;

functionDefinition
    : typeSpecifier ID LPAREN parameters? RPAREN LBRACE blockContent RBRACE
    ;

typeSpecifier
    : INT
    | CHAR
    | BOOL
    ;

parameters
    : parameter (COMMA parameter)*
    ;

parameter
    : typeSpecifier ID
    ;

blockContent
    : statement*
    ;

statement
    : variableDeclaration SEMICOLON
    | expression SEMICOLON // expressionStatement is just expression followed by SEMICOLON
    | ifStatement
    | whileStatement
    | forStatement
    | returnStatement SEMICOLON
    | LBRACE blockContent RBRACE // Nested block
    ;

variableDeclaration // Rule for 'int x;' or 'int x = 10;'
    : typeSpecifier ID (ASSIGN expression)?
    ;

ifStatement
    : IF LPAREN expression RPAREN statement (ELSE statement)?
    ;

whileStatement
    : WHILE LPAREN expression RPAREN statement
    ;

forStatement
    : FOR LPAREN forInitializer? SEMICOLON expression? SEMICOLON expression? RPAREN statement
    ;

forInitializer
    : variableDeclaration // For 'for(int i=0;...)' - variableDeclaration does not produce a semicolon here
    | expression          // For 'for(i=0;...)'
    ;

returnStatement
    : RETURN expression?
    ;

// Expression hierarchy to define precedence and associativity
expression
    : assignmentExpression
    ;

assignmentExpression
    : logicalOrExpression (ASSIGN expression)? // For 'x = y' or just 'y'
    ;

logicalOrExpression
    : logicalAndExpression (OR logicalAndExpression)*
    ;

logicalAndExpression
    : equalityExpression (AND equalityExpression)*
    ;

equalityExpression
    : relationalExpression ((EQ | NE) relationalExpression)*
    ;

relationalExpression
    : additiveExpression ((LT | LE | GT | GE) additiveExpression)*
    ;

additiveExpression
    : multiplicativeExpression ((PLUS | MINUS) multiplicativeExpression)*
    ;

multiplicativeExpression
    : unaryExpression ((TIMES | DIVIDE | MODULO) unaryExpression)*
    ;

unaryExpression
    : (PLUS | MINUS | NOT) unaryExpression
    | primaryExpression
    ;

primaryExpression
    : LPAREN expression RPAREN
    | ID
    | literal
    | functionCall
    ;

functionCall
    : ID LPAREN argumentList? RPAREN
    ;

argumentList
    : expression (COMMA expression)*
    ;

literal
    : NUMBER
    | CHAR_LITERAL
    | STRING_LITERAL
    | TRUE
    | FALSE
    ;

// --- LEXER RULES ---
INT: 'int';
CHAR: 'char';
BOOL: 'bool';
IF: 'if';
ELSE: 'else';
WHILE: 'while';
FOR: 'for';
RETURN: 'return';
TRUE: 'true';
FALSE: 'false';

ID: [a-zA-Z_] [a-zA-Z_0-9]*;
NUMBER: [0-9]+;
CHAR_LITERAL: '\'' ( ~['\\] | ('\\' .) ) '\''; // Allows escaped chars within ' '
STRING_LITERAL: '"' ( ~["\\] | ('\\' .) )*? '"'; // Allows escaped chars within " " (non-greedy)

LPAREN: '(';
RPAREN: ')';
LBRACE: '{';
RBRACE: '}';
SEMICOLON: ';';
COMMA: ',';
ASSIGN: '=';
GT: '>';
LT: '<';
GE: '>=';
LE: '<=';
EQ: '==';
NE: '!=';
AND: '&&';
OR: '||';
NOT: '!';
PLUS: '+';
MINUS: '-';
TIMES: '*';
DIVIDE: '/';
MODULO: '%';

WS: [ \t\r\n]+ -> skip;
LINE_COMMENT: '//' ~[\r\n]* -> skip; // Skips to end of line but not newline itself
// BLOCK_COMMENT: '/*' .*? '*/' -> skip; // If Mini-C supports block comments