# Exercicio 1
# A primeira proposta aqui é a seguinte faça um programa que peça ao usuário para digitar um número inteiro.
# Informe se este número par ou ímpar certo.
# E caso o usuário digite um caso o usuário não digite o número inteiro informe que o número não é um inteiro.

valor = input('Digite um numero Inteiro: ')
if valor.isnumeric():
    valor = int(valor)
    if valor % 2 == 0:
        print(f'{valor} é numero Par')
    else:
        print(f'{valor} é numero Impar')
else:
    print(f'Valor digitado {valor} não é um numero inteiro válido !!!')
