"""
Exercício
Exiba os índices da lista
0 Maria
1 Helena
2 Luiz
"""

lista = ['Maria', 'Helena', 'Luiz']
contador = 0

for nome in lista:
    print(contador, nome)
    contador += 1

print()

lista = ['Maria', 'Helena', 'Luiz']
indices = range(len(lista))

for indice in indices:
    print(indice, lista[indice])