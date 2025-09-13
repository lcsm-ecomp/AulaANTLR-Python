grammar Expr;

PRINT : 'print' ;
NUM : [0-9]+ ;
ID  : [a-z]+ ;
FOR : 'for' ;
OP1 : '+' | '-' ;
OP2 : '*' | '/' ;
AP  : '(' ;
FP  : ')' ;

SPACE : ([ \n\t\r]+) -> skip ;

programa : (c+=com)+ EOF ;

com : 'print' e=exp ';' #Print 
    | ID '=' exp ';' #Atrib 
    | 'for' ID '=' NUM 'to' NUM 'do' (c+=com)+ 'end'  #For ;

exp : valor=NUM #Const
    | nome=ID #Var
    | e=exp o=OP2 d=exp #Mult
    | e=exp o=OP1 d=exp #Soma
    | AP e=exp FP #Group
    ;