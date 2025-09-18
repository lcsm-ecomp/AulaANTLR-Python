from antlr4 import *
from ExprLexer import *
from ExprParser import *

"""
   As declaracoes contem uma relação de todas
   as variáveis declaradas e os seus respectivos
   tipos 
"""

declaracoes = { }

#Funcao que verifica se um programa é válido
#Levanta excessao caso erro.

def analise(t):
   match (t):
      case ExprParser.ProgramaContext():
         for dec in t.declaracoes:
              analise(dec)
         for com in t.comandos:
              analise(com)
      case ExprParser.DecContext():
           nome = t.nome.text
           if declaracoes.get(nome)!=None:
               raise Exception(f'variavel {nome} declarada duas vezes na linha {t.start.line}')   
           declaracoes[nome] = 'int'
      case ExprParser.AtribContext():
           nome = t.nome.text
           valor = t.valor
           if declaracoes.get(nome)==None:
               raise Exception(f'variavel {nome} nao foi declarada na atribuicao')
           analise(valor)
      case ExprParser.ForContext():
           nome = t.nome.text
           if declaracoes.get(nome)==None:
               raise Exception(f'variavel {nome} nao foi declarada no comando for')
           for com in t.c:
               analise(com)

      case ExprParser.ConstContext():
           t.valorNumerico = int(t.getText())
           return True
      case ExprParser.VarContext():
           nome = t.nome.text
           if declaracoes.get(nome)==None:
              raise Exception(f'variavel {nome} nao foi declarada na expressao')
      case TerminalNode():
           return True
      case _:
           for ch in t.getChildren():
              analise(ch)


