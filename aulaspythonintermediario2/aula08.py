# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.

def multiplicar(*args):
    total = 1
    for numero in args:
        total *= numero
    return total


valores = 1, 2, 3, 4, 5, 6
resultado = multiplicar(*valores)
print(f'Resultado da multiplicação dos {valores=} é {resultado}')


# Crie uma função fala se um número é par ou ímpar.
# Retorne se o número é par ou ímpar.

def par_impar(valor):
    if valor % 2 == 0:
        return 'Par'
    return 'Impar'

print(f'Valor 2 é {par_impar(2)}') 
print(f'Valor 10 é {par_impar(10)}')
print(f'Valor 5 é {par_impar(5)}')
print(f'Valor 13 é {par_impar(13)}')
print(f'Valor 21 é {par_impar(21)}')