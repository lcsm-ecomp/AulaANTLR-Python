from antlr4 import *
from ExprLexer import *
from ExprParser import *

#A memoria é uma funcao que retorna 
#o valor de cada variável
memoria = { }

#Funcao que executa um programa
def avalie(t):
   match t:
      case ExprParser.ProgramaContext():
           for x in t.comandos:
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
      case ExprParser.ConstNumContext():
           return t.valorNumerico
           return int(t.getChild(0).getText())
      case ExprParser.ConstStrContext():
           return t.valor.text[1:-1]
      case ExprParser.STRLengthContext():
           valor = avalie(t.e)
           return len(valor)
      case ExprParser.STRConcatContext():
           ve = avalie(t.e)
           vd = avalie(t.d)
           if isinstance(ve, str) and isinstance(vd,str):
              return ve+vd
           raise Exception("Erro de tipos do programa")
      case ExprParser.SomaContext():
           ve = avalie(t.e)
           vd = avalie(t.d)
           if isinstance(ve, int) and isinstance(vd,int):
              if t.getChild(1).getText()=='+':
                 return ve+vd
              else:
                 return ve-vd
           raise Exception("Erro de tipos na soma")

      case ExprParser.MultContext():
           ve = avalie(t.e)
           vd = avalie(t.d)
           if isinstance(ve, int) and isinstance(vd,int):
              if t.getChild(1).getText()=='*':
                 return ve*vd
              else:
                 return ve/vd
           raise Exception("Erro de tipos na multiplicacao")
      case ExprParser.GroupContext():
           return avalie(t.e)
      case ExprParser.VarContext():
           nome = t.getChild(0).getText()
           valor = memoria.get(nome)
           if valor==None:
               raise Exception(f"Variavel {nome} não definida")
           return valor
   raise Exception(f"não sei avaliar {t.getText()} ainda")	
