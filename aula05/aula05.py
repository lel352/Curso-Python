"""
Operadores Aritméticos
Adição: +
Subtração: -
Multiplicação: *
Divisão: /
Divisão Inteira: //
Exponenciação: **
Resto da Divisão: %
Precedência ()
"""
print('Adição 10 + 10 :', 10 + 10)
print('Subtração 10 - 10 :', 10 - 10)
print('Multiplicacao 10 * 10 :', 10 * 10)
print('Divisão 10 / 10 :', 10 / 10)
print('Divisão 10 / 3 :', 10 / 3)
print('Divisão Inteira 10 // 3 :', 10 // 3)
print('Divisão Inteira 10.5 // 3 :', 10.5 // 3)
print('Divisão Inteira 10.5 // 2.5 :', 10.5 // 2.5)
print('Exponenciação 10 ** 10: ', 10 ** 10)
print('Resto - modulo 10 % 10', 10 % 10)
print('Resto - modulo 10 % 3', 10 % 3)

#  Nesse caso o operador de multiplicação se comporta como um operador de repetição, Saída é 10 veze o '10'
print('10' * 10)
# Nesse caso o operador de Adição se tonar um operador de concatenação, Saída é '1010'
print('10' + '10')


# Precedência
print('5+2*10: ', 5+2*10)  # 1º = 2 * 10  2º = Resultado anterior + 10 = 2 * 10 = 20 + 5 = 25
print('(5+2)*10: ', (5+2)*10)  # 1º = (5 + 2)  2º = Resultado anterior * 10 = 5 + 2 = 7 * 10 = 70


"""
Assim como aprendemos na matemática, operadores têm uma certa precedência que pode ser alterada usando os parênteses 
(como descrito na aula anterior).

Abaixo, segue uma lista mais precisa de quais operadores tem maior prioridade na hora de realizar contas mais complexas
(de maior para menor precedência).

( n + n ) - Os parênteses têm a maior precedência, contas dentro deles são realizadas primeiro

** - Depois vem a exponenciação

* / //  % - Na sequência multiplicação, divisão, divisão inteira e módulo

+  - - Por fim, soma e subtração

Contas com operadores de mesma precedência são realizadas da esquerda para a direita.

Observação: existem muito mais operadores do que estes em Python e todos eles também têm precedência, você pode ver a
lista completa em https://docs.python.org/3/reference/expressions.html#operator-precedence
(sempre utilize a documentação oficial como reforço caso necessário).
"""