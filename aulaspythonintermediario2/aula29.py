# Introdução à List comprehension em Python
# List comprehension é uma forma rápida para criar listas
# a partir de iteráveis.
# print(list(range(10)))
import pprint


def p(v):
    pprint.pprint(v, sort_dicts=False, width=40)


lista = []
for numero in range(10):
    lista.append(numero)
# print(lista)

lista = [
    numero * 2
    for numero in range(10)
]
print(list(range(10)))
print(lista)
print()

# Mapeamento de dados em list comprehension
produtos = [
    {'nome': 'p1', 'preco': 20, },
    {'nome': 'p2', 'preco': 10, },
    {'nome': 'p3', 'preco': 30, },
]
novos_produtos = [
    {**produto, 'preco': produto['preco'] * 1.05}
    if produto['preco'] > 20 else {**produto}
    for produto in produtos
]

print(novos_produtos)
p(novos_produtos)
print()

lista = [n for n in range(10) if n < 5] # if vira um filtro
print(lista)
print()


print()

novos_produtos = [
    {**produto, 'preco': produto['preco'] * 1.05}
    if produto['preco'] > 20 else {**produto}
    for produto in produtos
    if produto['preco'] >= 20 and produto['preco'] * 1.05 > 10
]
p(novos_produtos)

print()
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
novo_numeros = [numero for numero in numeros if numero > 5]
impares = [numero for numero in numeros if numero % 2 != 0]
pares = [numero for numero in numeros if numero % 2 == 0]
outro_if = [
    numero
    if numero != 6 else 600
    for numero in pares
]

print(numeros)
print(novo_numeros)
print(impares)
print(pares)
print(outro_if)

print()
numeros = [[numero, numero ** 2] for numero in range(10)]
flat = [y for x in numeros for y in x]
print(numeros)
print(flat)