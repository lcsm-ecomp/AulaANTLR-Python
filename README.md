## Aula prática de ANTLR em Python

Estes arquivos contem a implementação de um estudo de caso para a disciplina de compiladores
no semestre 2025.2: Um compilador / interpretador de uma linguagem imperativa semelhante à linguagem C.

1. Arquivos:

- Expr.g4: Descrição Léxica e sintática da linguagem
- main.py: interpretador da linguagem 

2. Instalação
Utilizando python:
   - python -m venv .
   - .\Scripts\activate  # ou source ./bin/activate (pode variar de acordo com o SO)
   - pip install antlr4-tools antlr4-python3-runtime 
   
2. Execução do projeto
   - antlr4 -Dlanguage=Python3 Expr.g4
   - python main.py
   
