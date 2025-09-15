
# 1) Léxico (Tokens)

**(a) Descrição léxica**

Principais tokens (segundo o `.g4`):

* `PRINT` → `print`
* `FOR` → `for`
* `ID` → `[a-z]+`  (identificadores são letras minúsculas)
* `NUM` → `[0-9]+`  (inteiros decimais)
* `OP1` → `'+' | '-'`
* `OP2` → `'*' | '/'`
* `AP` → `'('`, `FP` → `')'`
* `SPACE` → espaços/brancos ignorados

**Observações:**

* Palavras‐chave: `print`, `for`, `to`, `do`, `end` (aparecem no código-fonte e na gramática, mesmo quando parte delas não esteja listada explicitamente nos trechos mostrados acima).
* Identificadores são *apenas* letras minúsculas (`a`–`z`), o que simplifica a gramática e o analisador.

**(b) —**
*(Não se aplica: esta seção é léxica, não há código do interpretador específico além do *lexer* gerado pelo ANTLR.)*

**(c) Explicação**

O ANTLR gera um *lexer* a partir dessas regras. O *lexer* transforma o texto de entrada em uma sequência de tokens, que depois é consumida pelo *parser*. Espaços e quebras de linha são ignorados. Numerais são inteiros positivos; não há sinal unário léxico — sinais aparecem como operadores binários em expressões.

---

# 2) Programa

**(a) Sintaxe (alto nível)**

Um **programa** é uma sequência de **comandos**, finalizados por `;` (no caso de comandos simples) ou `end` (no caso de blocos `for`). Ex.:

```plaintext
soma = 0 ;
for x = 1 to 100 do
  for y = 1 to 20 do
    soma = soma + x*y ;
  end
end
print soma ;
```

Regra de entrada do parser: `programa`.

**(b) Código do interpretador**

```python
# visita a árvore a partir da raiz (programa)
case ExprParser.ProgramaContext():
    for x in t.c:
        avalie(x)
    return
```

**(c) Explicação**

O interpretador (função `avalie`) recebe a raiz da árvore sintática e **itera** sobre a lista de comandos do programa (`t.c`), avaliando cada um em ordem. Não há valor de retorno do programa como um todo; efeitos ocorrem via **memória** (dicionário `memoria`) e `print`.

---

# 3) Atribuição

**(a) Sintaxe**

```plaintext
ID = expr ;
```

* `ID` é um identificador
* `expr` é qualquer expressão aritmética válida (ver Seção 6)

**(b) Código do interpretador**

```python
case ExprParser.AtribContext():
    nome = t.getChild(0).getText()
    valor = avalie(t.getChild(2))
    memoria[nome] = valor
    return
```

**(c) Explicação**

O nó de atribuição tem como filho 0 o nome da variável e como filho 2 a expressão à direita do `=`. O interpretador:

1. **Avalia** a expressão do lado direito
2. **Escreve** o resultado em `memoria[nome]`

Variáveis passam a existir na primeira atribuição. Caso sejam lidas antes de atribuídas, ocorre erro (ver “Variável”, Seção 6.2).

---

# 4) Comando `print`

**(a) Sintaxe**

```plaintext
print expr ;
```

**(b) Código do interpretador**

```python
case ExprParser.PrintContext():
    v = avalie(t.e)
    print(v)
    return
```

**(c) Explicação**

O interpretador **avalia** a expressão `expr` e envia o resultado para a saída padrão usando `print`. Não altera o estado de `memoria`.

---

# 5) Laço `for`

**(a) Sintaxe**

```plaintext
for ID = NUM to NUM do
   comandos...
end
```

* Limites são inteiros (`NUM`) e o laço é **inclusivo** em ambos os lados (ver implementação).
* O corpo é uma sequência de comandos (`comandos...`), normalmente com `;` ao final quando forem comandos simples.

**(b) Código do interpretador**

```python
case ExprParser.ForContext():
    nome  = t.getChild(1).getText()         # ID
    valorI = int(t.getChild(3).getText())   # NUM inicial
    valorF = int(t.getChild(5).getText())   # NUM final
    for v in range(valorI, valorF + 1):     # inclusivo!
        memoria[nome] = v
        for x in t.c:
            avalie(x)
    return
```

**(c) Explicação**

O laço `for` percorre o intervalo **\[início, fim]** *inclusive*. A cada iteração:

1. A variável de controle `ID` recebe o valor atual `v` (é atualizada na `memoria`)
2. Cada comando do corpo (`t.c`) é avaliado na ordem

Não há valor de retorno. Se o limite inferior for maior que o superior, o laço não executa (sem erro).

---

# 6) Expressões Aritméticas

A gramática suporta constantes, variáveis, agrupamento com parênteses e operadores binários com precedência usual:

* **Precedência**: `*` e `/` (alta) > `+` e `-` (baixa)
* **Associatividade**: esquerda (por padrão, na construção recursiva da gramática)

As **classes de nós** no parser sugerem as seguintes formas: `Const`, `Var`, `Group`, `Mult` (/\*), `Soma` (+/-).

## 6.1) Constante Numérica

**(a) Sintaxe**

```plaintext
NUM
```

**(b) Código do interpretador**

```python
case ExprParser.ConstContext():
    return int(t.getChild(0).getText())
```

**(c) Explicação**

Converte o lexema numérico para `int` e retorna o valor.

---

## 6.2) Variável

**(a) Sintaxe**

```plaintext
ID
```

**(b) Código do interpretador**

```python
case ExprParser.VarContext():
    nome  = t.getChild(0).getText()
    valor = memoria.get(nome)
    if valor == None:
        raise Exception(f"Variavel {nome} não definida")
    return valor
```

**(c) Explicação**

Busca o valor atual do identificador em `memoria`. Se ainda não houve atribuição àquela variável, o interpretador lança uma exceção (**variável não definida**).

---

## 6.3) Agrupamento

**(a) Sintaxe**

```plaintext
( expr )
```

**(b) Código do interpretador**

```python
case ExprParser.GroupContext():
    return avalie(t.e)
```

**(c) Explicação**

Apenas **repassa** a avaliação da subexpressão `e`, garantindo a precedência desejada.

---

## 6.4) Multiplicação e Divisão

**(a) Sintaxe**

```plaintext
expr OP2 expr   # com OP2 ∈ {'*', '/'}
```

**(b) Código do interpretador**

```python
case ExprParser.MultContext():
    ve = avalie(t.e)  # operando esquerdo
    vd = avalie(t.d)  # operando direito
    if t.getChild(1).getText() == '*':
        return ve * vd
    else:
        return ve / vd
```

**(c) Explicação**

Avalia os dois operandos e aplica `*` ou `/`.
**Atenção:** a divisão é `vd` *não inteira* em Python; pode produzir `float`. Divisão por zero gera exceção do Python.

---

## 6.5) Soma e Subtração

**(a) Sintaxe**

```plaintext
expr OP1 expr   # com OP1 ∈ {'+', '-'}
```

**(b) Código do interpretador**

```python
case ExprParser.SomaContext():
    ve = avalie(t.e)
    vd = avalie(t.d)
    if t.getChild(1).getText() == '+':
        return ve + vd
    else:
        return ve - vd
```

**(c) Explicação**

Avalia os dois operandos e retorna a soma ou a diferença.

---

# 7) Execução, Ambiente e Erros

* **Memória**: um dicionário global `memoria = {}` mapeia `ID → valor`.
* **Fluxo**: `programa` → percorre comandos; cada comando altera `memoria` e/ou imprime.
* **Erros comuns**:

  * **Sintaxe**: interrompe a execução se o parser reportar `getNumberOfSyntaxErrors() > 0`.
  * **Variável não definida**: ao usar um `ID` que nunca recebeu valor (Seção 6.2).
  * **Divisão por zero**: propagada pelo Python (Seção 6.4).

---

# 8) Exemplo completo

**Fonte:**

```plaintext
soma = 0 ;
for x = 1 to 100 do
  for y = 1 to 20 do
    soma = soma + x*y ;
  end
end
print soma ;
```

**Saída esperada:**

```
1060500
```

*(porque $\sum_{x=1}^{100} x \cdot \sum_{y=1}^{20} y = (100·101/2) · (20·21/2) = 5050 · 210 = 1060500$)*

---

# 9) Gabarito mínimo da gramática (esboço)

Para referência — um **esqueleto** coerente com os *contexts* usados pelo interpretador (nomes podem variar conforme seu `.g4` real):

```antlr
grammar Expr;

programa
  : comando* EOF
  ;

comando
  : ID '=' expr ';'                     # Atrib
  | PRINT expr ';'                      # Print
  | FOR ID '=' NUM 'to' NUM 'do' c+=comando* 'end'   # For
  ;

expr
  : expr OP1 expr                       # Soma
  | expr OP2 expr                       # Mult
  | AP expr FP                          # Group
  | NUM                                 # Const
  | ID                                  # Var
  ;

// LÉXICO (conforme Seção 1)
// PRINT: 'print'; FOR: 'for';
// OP1: '+' | '-'; OP2: '*' | '/';
// AP: '('; FP: ')';
// ID: [a-z]+; NUM: [0-9]+;
// SPACE: [ \t\r\n]+ -> skip;
```

> Observação: em um `.g4` real, você provavelmente usará **precedência**/associatividade por meio de regras fatoradas (por exemplo, `termo`, `fator`) ou **operadores precedenciais** com `assoc=left`. O esboço acima foi mantido simples para corresponder aos *contexts* presentes no seu interpretador.

---

# 10) Como estender

* **Relacionais/booleanos**: adicionar `<, <=, ==, !=, and, or`, e um comando `if ... then ... [else ...] end`.
* **Entrada**: uma função `read()` como expressão para ler valores.
* **Variável de laço imutável**: impedir escrita à variável de controle dentro do `for`.
* **Escopos**: permitir blocos com escopo léxico (sombras de nomes).

---

Se quiser, eu gero uma versão desta documentação em **PDF** ou em **Markdown/Reveal.js** para suas aulas, com tabelas de precedência e diagrama sintático. Também posso sincronizar a gramática real do seu `Expr.g4` (se tiver regras adicionais) e alinhar os nomes dos *contexts* exatamente.

