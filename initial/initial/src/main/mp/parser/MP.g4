//
//Student name: Nguyen Thi Tuong Vy
// Student ID: 1414796
//


grammar MP;

@lexer::header {
from lexererr import *
}

options{
	language=Python3;
}



program: decl+ EOF;

decl: varDecls | funcDecls | proceDecls;

varDecls: VAR varDecl+;

varDecl: ID (COMMA ID)* COLON (primiType | arrayType) SEMI;

primiType: INTLIT | FLOATLIT | BOOLEANLIT | STRINGLIT;

arrayType: ARRAY LSB expr DOUBLEDOT expr RSB OF primiType;

funcDecls: FUNCTION ID LB paraList? RB COLON (primiType | arrayType) SEMI varDecls? compoundStm;

paraList: param (SEMI param)*; 

param: ID (COMMA ID)* COLON (primiType | arrayType);

stmt: assignmentStm | ifStm | forStm |  whileStm | breakStm | continueStm | returnStm | callStm | compoundStm | withStm;

assignmentStm: (leftSide COEQ)+ expr SEMI;

leftSide: ID | expr (LSB expr RSB);

ifStm: IF expr THEN stmt (ELSE stmt)?;

forStm: FOR ID COEQ expr (TO | DOWNTO) expr DO stmt;

whileStm: WHILE expr DO stmt;

breakStm: BREAK SEMI;

continueStm: CONTINUE SEMI;

returnStm: RETURN SEMI| RETURN expr SEMI;

compoundStm: BEGIN stmt* END;

withStm: WITH varDecl+ DO stmt;

funcall: ID LB (expr (COMMA expr)*)? RB;

callStm: funcall SEMI;

expr: expr AND expr1
	| expr THEN expr1
	| expr OR expr1
	| expr ELSE expr1
	| expr1;

expr1: expr2 EQUA expr2
	| expr2 NOEQ expr2
	| expr2 LTHA expr2
	| expr2 LOEQ expr2
	| expr2 GTHA expr2
	| expr2 GOEQ expr2
	| expr2;

expr2: expr2 ADD expr3
	| expr2 SUB expr3
	| expr3;

expr3: expr3 DIVI expr4
	| expr3 MUL expr4
	| expr3 DIV expr4
	| expr3 MOD expr4
	| expr4;

expr4: NOT expr4
	| SUB expr4
	| expr5;

expr5: expr6 LSB expr RSB
	| expr6;

expr6: INTLIT | FLOATLIT | BOOLEANLIT | STRINGLIT | ID | LB expr RB | funcall;

proceDecls: PROCEDURE ID LB paraList? RB SEMI varDecls? compoundStm;

////////////////////////
// program: declaration+ EOF; 
// declaration: vardec | funcdec |prodec;
// vardec : VAR declist+;
// declist : ID (CM ID)* CL mptype SEMI ;
// mptype: primitiveType |compoundtype ;
// primitiveType
//     :   BOOLEAN
//     |   INTTYPE
//     |   FLOATTYPE
//     |   STRING
//     ;
// compoundtype : ARRAY LSB expr DD expr RSB OF primitiveType;
// funcdec: FUNCTION ID LB paralist RB CL mptype SEMI vardec? compound_stmt;
// paralist: (paradec ( SEMI paradec )*)? ;
// paradec: ID (CM ID)* CL mptype;
// prodec: PROCEDURE ID LB paralist RB SEMI vardec? compound_stmt;


// expr  	: expr (AND|THEN|OR|ELSE) expr1
// 		| expr1;
// expr1 	: expr2 (EQUAL_OP|NOT_EQ_OP|LT_OP|LE_OP|GT_OP|GE_OP) expr2
// 		| expr2;
// expr2 	: expr2 (ADD_OP|SUB_OP|OR)  expr3
// 		| expr3;	
// expr3 	: expr3 (DIV_OP|MUL_OP|MOD|DIV|AND|) expr4
// 		| expr4;
// expr4 	:(SUB_OP|NOT) expr4
// 		| expr5;
// expr5   : term LSB expr RSB | term;
// term 	: ID
// 		| INTLIT
// 		| FLOATLIT
// 		| BOOLLIT
// 		| STRINGLIT 
// 		| LB expr RB
// 		| funcall;

// stmt: if_stmt
// 	|assign_stmt
// 	|for_stmt
// 	|while_stmt
// 	|break_stmt
// 	|continue_stmt
// 	|return_stmt
// 	|call_stmt
// 	|compound_stmt
// 	|with_stmt;
// assign_stmt: (lhs ASS_OP )+ expr SEMI ;

// lhs: ID |expr  LSB expr RSB ;
// if_stmt: IF expr THEN stmt (ELSE stmt)?;
// while_stmt: WHILE expr DO stmt;
// for_stmt: FOR ID ASS_OP expr (TO|DOWNTO) expr DO stmt ;
// break_stmt: BREAK SEMI;
// continue_stmt: CONTINUE SEMI;
// return_stmt : RETURN expr? SEMI;
// compound_stmt: BEGIN stmt* END;
// with_stmt: WITH declist+ DO stmt ;
// call_stmt: funcall SEMI ;
// indexExp: (ID | funcall) LSB expr RSB;
// funcall : ID LB (expr (CM expr)*)? RB;


///////////////////

INTLIT: [-]?[0-9]+;

// FLOATLIT: [+-](([0-9]*'.'[0-9]*)[^(0'.'0)])([Ee][+-]?[1-9][0-9]*)?;

fragment DIGI  : [0-9];
fragment EXP : [Ee][-]?DIGI+;
 
FLOATLIT : DIGI+ EXP
		 | DIGI* '.' DIGI+ EXP?
		 | DIGI+ '.' DIGI* EXP?;

BOOLEANLIT: [Tt][Rr][Uu][Ee]| [Ff][Aa][Ll][Ss][Ee];

COEQ: ':=';

LB: '(' ;

RB: ')' ;

LP: '{';

RP: '}';

LSB: '[';

RSB: ']';

COLON: ':';

DOUBLEDOT: '..';

COMMA: ',';

SEMI: ';' ;

ADD: '+';

MUL: '*';

KNOT: 'not';

KOR: 'or';

NOEQ: '<>';

LTHA: '<';

LOEQ: '<=';

KDIV: 'div';

SUB: '-';

DIVI: '/';

KMOD: 'mod';

KAND: 'and';

EQUA: '=';

GTHA: '>';

GOEQ: '>=';


WITH: [Ww][Ii][Tt][Hh];

BREAK: [Bb][Rr][Ee][Aa][Kk];

CONTINUE: [Cc][Oo][Tt][Ii][Nn][Uu][Ee];

FOR: [Ff][Oo][Rr];

TO: [Tt][Oo];

DOWNTO: [Dd][Oo][Ww][Nn][Tt][Oo];

DO: [Dd][Oo];

IF: [Ii][Ff];

THEN: [Tt][Hh][Ee][Nn];

ELSE: [Ee][Ll][Ss][Ee];

RETURN: [Rr][Ee][Tt][Uu][Rr][Nn];

WHILE: [Ww][Hh][Ii][Ll][Ee];

BEGIN: [Bb][Ee][Gg][Ii][Nn];

END: [Ee][Nn][Dd];

FUNCTION: [Ff][Uu][Nn][Cc][Tt][Ii][Oo][Nn];

PROCEDURE: [Pp][Rr][Oo][Cc][Ee][Dd][Uu][Rr][Ee];

VAR: [Vv][Aa][Rr];

TRUE: [Tt][Rr][Uu][Ee];

FALSE: [Ff][Aa][Ll][Ss][Ee];

ARRAY: [Aa][Rr][Rr][Aa][Yy];

OF: [Oo][Ff];

REAL: [Rr][Ee][Aa][Ll];

BOOLEAN: [Bb][Oo][Oo][Ll][Ee][Aa][Nn];

INTEGER: [Ii][Nn][Tt][Ee][Gg][Ee][Rr];

STRING: [Ss][Tt][Rr][Ii][Nn][Gg];

NOT: [Nn][Oo][Tt];

AND: [Aa][Nn][Dd];

OR: [Oo][Rr];

DIV: [Dd][Ii][Vv];

MOD: [Mm][Oo][Dd];

fragment PREFIX_STRING: (~('"'|'\n'|'\r'|'\\'));
fragment SUPPORTED_ESCAPE: '\\'('b'|'f'|'r'|'n'|'t'|'\''|'"'|'\\');
//STRINGLIT: '"'(PREFIX_STRING|SUPPORTED_ESCAPE)*'"' {setText(getText().substring(1, getText().length()-1));};
STRINGLIT: '"'( SUPPORTED_ESCAPE | ~["\\\n\r\t])*{self.text = self.text[1:]}'"';

ID: [a-zA-Z_][a-zA-Z0-9_]* ;

// BLOCK_COMMENT: [('(*'.*?('*)'))('{'.*?('}'))] -> skip;
// LINE_COMMENT: '//'~[\r\n\f]* -> skip;

TRCMT: '(*'.*?'*)'->skip;

BCMT: '{'.*?'}'->skip;

LCMT: '//'.*?~[\r\n]*->skip;

WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines



ERROR_CHAR: . {raise ErrorToken(self.text)};
UNCLOSE_STRING: . {raise UncloseString(self.text[1:])};
ILLEGAL_ESCAPE: . {raise IllegalEscape(self.text)};