from antlr4 import *
from ExprLexer import *
from ExprParser import *

src = """
  soma = 0 ;
  for x = 1 to 100 do
     for y = 1 to 20 do
        soma = soma + x*y ;
     end
  end
  print soma ;
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

memoria = { }
def avalie(t):
   match t:
      case ExprParser.ProgramaContext():
           for x in t.c:
             avalie(x)
           return
      case ExprParser.AtribContext():
           nome = t.getChild(0).getText()
           valor = avalie(t.getChild(2))
           memoria[nome] = valor
           return
      case ExprParser.PrintContext():
           v = avalie(t.e)
           print(v)
           return
      case ExprParser.ForContext():
           nome = t.getChild(1).getText()
           valorI = int(t.getChild(3).getText())
           valorF = int(t.getChild(5).getText())
           for v in range(valorI,valorF+1):
               memoria[nome] = v
               for x in t.c:
                  avalie(x)	
           return
      case ExprParser.ConstContext():
           return int(t.getChild(0).getText())
      case ExprParser.SomaContext():
           ve = avalie(t.e)
           vd = avalie(t.d)
           if t.getChild(1).getText()=='+':
              return ve+vd
           else:
              return ve-vd
      case ExprParser.MultContext():
           ve = avalie(t.e)
           vd = avalie(t.d)
           if t.getChild(1).getText()=='*':
              return ve*vd
           else:
              return ve/vd
      case ExprParser.GroupContext():
           return avalie(t.e)
      case ExprParser.VarContext():
           nome = t.getChild(0).getText()
           valor = memoria.get(nome)
           if valor==None:
               raise Exception(f"Variavel {nome} não definida")
           return valor
   raise Exception(f"não sei avaliar {t.getText()} ainda")	

print("Executando o programa...")
avalie(tree)



