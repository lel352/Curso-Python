'''Aula 15 - Combinations, Permutations e Product - Itertools
Combinations - Ordem não importa - Combinação
Permutations - Ordem importa - Permutação
Ambos não repetem valores únicos
Product - Ordem importa e repete valores únicos - Produto
'''

from itertools import combinations, permutations, product

pessoas = ['Luiz', 'André', 'Eduardo', 'Maria', 'Fabrício', 'Leandro', 'Juliane']

# A ordem não importa, ou seja, não repete ex: (Luiz, André) não vai ter o (André, Luiz)
for grupo in combinations(pessoas, 2):  # combinação em grupo de 2
    print(grupo)

# A ordem importa, ou seja, repete ex: (Luiz, André) assim vai ter o (André, Luiz)
for grupo in permutations(pessoas, 2):  # Permutação em grupo de 2
    print(grupo)

# A ordem importa, ou seja, repete valores ex: (Luiz, André) assim vai ter o (André, Luiz)
# como vai ter repetição com nomes iguais, ex (Luiz, Luiz)
for grupo in product(pessoas, repeat=2):  # Produto em grupo de 2
    print(grupo)


for grupo in combinations(pessoas, 3):  # combinação em grupo de 3
    print(grupo)