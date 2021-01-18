"""
Zip - Unindo Interáveis
zip_longest - itertools
"""

from itertools import zip_longest, count

indice = count() # contar de zero em 1 em 1
cidades = ['São Paulo', 'Belo Horizonte', 'Salvador', 'Criciúma']
estados = ['SP', 'MG', 'BA']

# zip uni com a menos list, ou seja ps estados assim gera um interável com 3 dados
cidade_estados = zip(cidades, estados)
for valor in cidade_estados:
    print(valor)


estados_cidades = zip(estados, cidades)
print(dict(estados_cidades ))
for valor in estados_cidades:
    print(valor)


estados_cidades = zip(estados, cidades, estados)
print(list(estados_cidades))


# ele preenche com none onde não tem valor.
cidade_estados = zip_longest(cidades, estados)
print(list(cidade_estados))


# fillvalue é valor default em vem de 'none' Gerrador
cidade_estados = zip_longest(cidades, estados, fillvalue='Estado')
print(list(cidade_estados))


cidade_estados = zip(
    indice,
    estados,
    cidades
)
for valor in cidade_estados:
    print(valor)
    
for indice, estado, cidade in cidade_estados:
    print(indice, estado, cidade)

