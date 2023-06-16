# Introdução à função lambda (função anônima de uma linha)
# A função lambda é uma função como qualquer
# outra em Python. Porém, são funções anônimas
# que contém apenas uma linha. Ou seja, tudo
# deve ser contido dentro de uma única
# expressão.

lista = [4, 32, 1, 34, 5, 6, 6, 21, ]
print(lista)
lista.sort()
print(lista)
lista.sort(reverse=True)
# sorted(lista) # copia rasa
print()

def exibir(lista):
    for item in lista:
        print(item)
    print()


lista = [
    {'nome': 'Leandro', 'sobrenome': 'Sartor'},
    {'nome': 'Maria', 'sobrenome': 'Oliveira'},
    {'nome': 'Daniel', 'sobrenome': 'Silva'},
    {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
    {'nome': 'Aline', 'sobrenome': 'Souza'},
]
exibir(lista)
print()


l1 = sorted(lista, key=lambda item: item['nome']) # copia rasa.
l2 = sorted(lista, key=lambda item: item['sobrenome'])

exibir(l1)
exibir(l2)
exibir(lista)

def orderna(item):
    return item['nome'] 
# ou lambda item: item['nome'])

lista.sort(key=orderna)
exibir(lista)
