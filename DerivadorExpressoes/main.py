from antlr4 import *
from ExprLexer import *
from ExprParser import *

#Funcoes de Geracao de Código

#Gera o codigo fonte a partir da árvore sintática
def unParse(t):
   match t:
      case ExprParser.PotContext():
         return "("+unParse(t.e)+")^("+unParse(t.d)+")"
      case ExprParser.MulContext():
         return "("+unParse(t.e)+")"+t.op.text+"("+unParse(t.d)+")"
      case ExprParser.SomContext():
         return "("+unParse(t.e)+")"+t.op.text+"("+unParse(t.d)+")"
      case ExprParser.ConstContext():
         return t.valor.text
      case ExprParser.VarXContext():
         return 'x'
      case ExprParser.GroupContext():
         return "("+unParse(t.e)+")"
    
#Avalia uma expressao
def avalie(t,x):
   match t:
      case ExprParser.PotContext():
         return avalie(t.e,x)**avalie(t.d,x)
      case ExprParser.MulContext():
         if t.op.text=="*":
            return avalie(t.e,x) * avalie(t.d,x)
         else:
            return avalie(t.e,x) / avalie(t.d,x)
      case ExprParser.SomContext():
         if t.op.text=="+":
            return avalie(t.e,x) + avalie(t.d,x)
         else:
            return avalie(t.e,x) - avalie(t.d,x)
      case ExprParser.ConstContext():
         return float(t.valor.text)
      case ExprParser.VarXContext():
         return x
      case ExprParser.GroupContext():
         return avalie(t.e,x)

#Calcula a derivada de uma função retorna a string da expressao:
def deriva(t):
   match t:
      case ExprParser.PotContext():
         if isinstance(t.d, ExprParser.ConstContext):
            exp = float(t.d.getText())
            if isinstance(t.e,ExprParser.VarXContext):
               return f"{exp}*X^{exp-1}"
            else: 
               return f"{exp}*({unParse(t.e)})^{exp-1}*({deriva(t.e)})"


         raise Exception("Esta expressao é muito complicada....")
      case ExprParser.MulContext():
         if t.op.text=="*":
            if isinstance(t.e,ExprParser.ConstContext):
               return f"({unParse(t.e)})*{deriva(t.d)}"
            if isinstance(t.d,ExprParser.ConstContext):
               return f"({unParse(t.d)})*{deriva(t.e)}"
            return f"({deriva(t.e)})*{unParse(t.d)} + ({unParse(t.e)})*{deriva(t.d)}"
         else:
            return f"(({deriva(t.e)})*({unParse(t.d)}) - ({unParse(t.e)})*({deriva(t.d)}) ))/(({unParse(t.d)})^2)"
      case ExprParser.SomContext():
         if t.op.text=="+":
            return "("+deriva(t.e) + ")+(" + deriva(t.d) + ")"
         else:
            return "("+deriva(t.e) + ")-(" + deriva(t.d) + ")"
      case ExprParser.ConstContext():
         return "0"
      case ExprParser.VarXContext():
         return "1"
      case ExprParser.GroupContext():
         return deriva(t.e)

def token(str):
   result = Token()
   result.text = str
   return result

#Calcula a derivada de uma função retorna uma árvore representando a derivada da expressao:
def derivaV2(t):
   def soma(e,op,d):
      result = ExprParser.SomContext(parser,t)
      result.op = token(op)
      result.e = e
      result.d = d
      return result
   def produto(e,op,d):
      result = ExprParser.MulContext(parser,t)
      result.op = token(op)
      result.e = e
      result.d = d
      return result
   def potencia(e,d):
      result = ExprParser.PotContext(parser,t)
      result.op = token('^')
      result.e = e
      result.d = d
      return result
   def constante(c):
      result = ExprParser.ConstContext(parser,t)
      result.valor = token(str(c))
      return result
   
   match t:
      case ExprParser.PotContext():
         if isinstance(t.d, ExprParser.ConstContext):
            exp = float(t.d.valor.text)
            if isinstance(t.e,ExprParser.VarXContext):
               return produto(
                  t.d,
                  '*',
                  potencia(t.e, constante(exp-1))
               )
            #f"{exp}*X^{exp-1}
            else: 
               return f"{exp}*({unParse(t.e)})^{exp-1}*({deriva(t.e)})"


         raise Exception("Esta expressao é muito complicada....")
      case ExprParser.MulContext():
         if t.op.text=="*":
            return soma(
               produto(derivaV2(t.e),'*', t.d),
               '+',
               produto(t.e, '*', derivaV2(t.d))
            )
         else:
            return produto(
               soma(
                  produto(
                     derivaV2(t.e),
                     '*',
                     t.d
                  ),
                  '-',
                  produto(
                     t.e,
                     '*',
                     derivaV2(t.d)
                  )
               ),
               '/',
               potencia(t.d, constante('2'))
                  
               )
      case ExprParser.SomContext():
            return soma(derivaV2(t.e), '+', derivaV2(t.d))
      case ExprParser.ConstContext():
         result = ExprParser.ConstContext(parser,t)
         result.valor = Token()
         result.valor.text = "0"
         return result
      case ExprParser.VarXContext():
         result = ExprParser.ConstContext(parser,t)
         result.valor = Token()
         result.valor.text = "1"
         return result
      case ExprParser.GroupContext():
         return deriva(t.e)


src = "2 * x ^ 2"
input_stream = InputStream(src)
lexer = ExprLexer(input_stream)
token_stream = CommonTokenStream(lexer)

parser = ExprParser(token_stream)

tree = parser.start()
if parser.getNumberOfSyntaxErrors()>0:
   raise Exception("Erro de sintaxe")
   
print("Programa ok")
tree = tree.getChild(0)
print("Codigo Recontruido: " + unParse(tree))
print(f"f(2) = {avalie(tree,2)}")
print(f"Sua funcao derivada: {deriva(tree)}")
print(f"Sua funcao derivada: {unParse(derivaV2(tree))}")
