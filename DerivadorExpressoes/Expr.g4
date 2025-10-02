grammar Expr;

BRANCOS : (' '|'\n'|'\t') -> skip; 
NUM : [0-9]+('.'[0-9]+)? ;
OPM : '*' | '/' ;
OPS : '+' | '-' ;

start : exp EOF ;

exp : e=exp op='^' d=exp #Pot
    | e=exp op=OPM d=exp #Mul
    | e=exp op=OPS d=exp #Som
    | valor=NUM #Const
    | 'x' #VarX
    | '(' e=exp ')' #Group
    ;

