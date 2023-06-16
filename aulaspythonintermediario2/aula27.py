# Introdução à List comprehension em Python
# List comprehension é uma forma rápida para criar listas
# a partir de iteráveis.
# print(list(range(10)))
lista = []
for numero in range(10):
    lista.append(numero)
# print(lista)

lista = [
    numero * 2
    for numero in range(10)
]
print(lista)

lista = [numero for numero in range(10)]
print(lista)


def divisãoFn(x, y):
    return x / y


def multiplicaçãoFn(x, y):
    return x * y


def potenciaçãoFn(x, y):
    return x ** y


numeros = [1, 2, 3, 4, 5]
divisão = [divisãoFn(numero, 2) for numero in numeros]
multiplicação = [multiplicaçãoFn(numero, 2) for numero in numeros]
quadrado = [potenciaçãoFn(numero, 2) for numero in numeros]

print(numeros)
print(divisão)
print(multiplicação)
print(quadrado)
