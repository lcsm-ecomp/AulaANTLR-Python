from antlr4 import *
from ExprLexer import *
from ExprParser import *

#Guarda o primeiro endereco da memória livre para uso
enderecoLivre = 1024

#Guarda o endereco onde todas as variaveis declaradas estão armazenadas
#Exemplo: {x -> 1028, y -> 1032}
variaveisAlocadas = { }

#Funcao que executa um programa
def gera_codigo(t):
   global enderecoLivre
   match t:
      case ExprParser.ProgramaContext():
           #Gera codigo para declarações e comandos do programa
           for d in t.declaracoes:
              gera_codigo(d)
           for c in t.comandos:
             gera_codigo(c)
           return
      case ExprParser.DecContext():
         tipo = t.tipo.text
         nome = t.nome.text
         variaveisAlocadas[nome] = enderecoLivre
         if tipo=="Int":
             enderecoLivre = enderecoLivre + 4
         elif tipo=="String":
             enderecoLivre = enderecoLivre + 256
         else:
             raise Exception(f"Nao conheco o tipo {tipo}")
         print(f"; reservado o endereco {variaveisAlocadas[nome]} para a variavel {nome}")
         return
      case ExprParser.AtribContext():
         nome = t.nome.text
         valor = t.valor
         endereco = variaveisAlocadas[nome]
         print(f"PUSHI {endereco} ;O endereco de {nome}")
         print(f";calcula o valor de {valor.getText()}")
         gera_codigo(valor)
         print("STORE")
      case ExprParser.PrintContext():
         gera_codigo(t.e)
         print("PRINT")
      case ExprParser.ConstNumContext():
         print(f"PUSHI {t.valor.text}")
         return     
      case ExprParser.SomaContext():
         esq = t.e
         dir = t.d
         op = t.o.text
         gera_codigo(esq)
         gera_codigo(dir)
         if op=="+":
            print("ADD")
         else:
             print("SUB")
         return
      case ExprParser.MultContext():
         esq = t.e
         dir = t.d
         op = t.o.text
         gera_codigo(esq)
         gera_codigo(dir)
         if op=="*":
            print("MUL")
         else:
             print("DIV")
         return
      case ExprParser.VarContext():
         nome = t.nome.text
         end = variaveisAlocadas[nome]
         print(f"PUSHI {end} ;endereco de {nome}")
         print("LOAD")
      case ExprParser.GroupContext():
         gera_codigo(t.e)
      case _:         
         raise Exception(f"não sei gerar o código de {t.getText()} ainda")	
