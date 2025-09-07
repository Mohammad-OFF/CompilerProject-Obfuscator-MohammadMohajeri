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

breakStatement
    : BREAK SEMICOLON
    ;

// Updated statement rule to include switch, case, and break statements
statement
    : variableDeclaration SEMICOLON
    | expression SEMICOLON
    | ifStatement
    | whileStatement
    | forStatement
    | returnStatement SEMICOLON
    | LBRACE blockContent RBRACE
    | switchStatement // New rule for switch
    | BREAK SEMICOLON // New rule for break
    ;

variableDeclaration
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
    : variableDeclaration
    | expression
    ;

returnStatement
    : RETURN expression?
    ;

// New rule for a switch statement. It expects a LBRACE/RBRACE block containing case and default rules.
switchStatement
    : SWITCH LPAREN expression RPAREN LBRACE caseStatement* defaultStatement? RBRACE
    ;

// New rule for a case statement. A case has a literal value and a body of statements.
caseStatement
    : CASE literal COLON statement+
    ;

// New rule for the default case.
defaultStatement
    : DEFAULT COLON statement+
    ;

// Expression hierarchy
expression
    : assignmentExpression
    ;

assignmentExpression
    : logicalOrExpression (ASSIGN expression)?
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
SWITCH: 'switch'; // New
CASE: 'case';     // New
DEFAULT: 'default'; // New
BREAK: 'break';   // New

ID: [a-zA-Z_] [a-zA-Z_0-9]*;
NUMBER: [0-9]+;
CHAR_LITERAL: '\'' ( ~['\\] | ('\\' .) ) '\'';
STRING_LITERAL: '"' ( ~["\\] | ('\\' .) )*? '"';

LPAREN: '(';
RPAREN: ')';
LBRACE: '{';
RBRACE: '}';
SEMICOLON: ';';
COMMA: ',';
COLON: ':'; // New
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
LINE_COMMENT: '//' ~[\r\n]* -> skip;