grammar Expr;

TYPE : 'Int' | 'String' ; 
FOR : 'for' ;
VAR : 'var' ;
PRINT : 'print' ;
NUM : [0-9]+ ;
STR : '"' (~'"')* '"' ;
ID  : [a-z]+ ;
OP1 : '+' | '-' ;
OP2 : '*' | '/' ;
AP  : '(' ;
FP  : ')' ;

SPACE : ([ \n\t\r]+) -> skip ;

programa : (declaracoes+=dec)* (comandos+=com)+ EOF ;

dec : tipo=TYPE nome=ID ';' ;

com : 'print' e=exp ';' #Print 
    | nome=ID '=' valor=exp ';' #Atrib 
    | 'for' nome=ID '=' NUM 'to' NUM 'do' (c+=com)+ 'end'  #For ;

exp : valor=NUM #ConstNum
    | valor=STR #ConstStr
    | nome=ID #Var
    | '#' e=exp #STRLength
    | e=exp '++' d=exp #STRConcat
    | e=exp o=OP2 d=exp #Mult
    | e=exp o=OP1 d=exp #Soma
    | AP e=exp FP #Group
    ;