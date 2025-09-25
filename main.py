from antlr4 import *
from ExprLexer import *
from ExprParser import *
from interpretador import *
from analisador_semantico import *

src = """
  var soma ;
  var x ;
  var z ;
  soma = 0 ;
  for x = 1 to 100 do
     for z = 1 to 20 do
        soma = soma + x*z +  1;
     end
  end
  print soma    ;
"""
src = """
   String msg;
   Int valor ;
   valor = "1" ;
   print(valor) ;
   msg = "ola mundo";
   print msg ;
   print #msg ;
   msg = msg ++ ", bom dia a todos" ;
   print msg;
   msg = msg  ;
   print msg;
"""
src = """
   String msg;
   Int valor ;
   valor = 1 ;
   msg = "a" ;
   msg = "1" ++ msg ; 
"""
input_stream = InputStream(src)
lexer = ExprLexer(input_stream)
token_stream = CommonTokenStream(lexer)

parser = ExprParser(token_stream)

tree = parser.programa()
if parser.getNumberOfSyntaxErrors()>0:
   raise Exception("Erro de sintaxe")
   
print("Programa ok")
if False:
   print(tree.toStringTree(recog=parser))
   #tree = tree.getChild(0)
   print(f"Este no possui {tree.getChildCount()} branches")
   for x in range(tree.getChildCount()):
      print(f"Filho {x} = {tree.getChild(x).getText()}")


print("Analisando o programa")
analise(tree)

print("Executando o programa...")
avalie(tree)



