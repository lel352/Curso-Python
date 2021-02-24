# reduce -  acumular valores
from aulaspythonintermediario.aula17.dados import lista, pessoas, produtos

from functools import reduce

acumula = 0
for item in lista:
    acumula += item

print(acumula)

#variável ac - pegando o item I - explessão - lista valores - incia o ac em zero
soma_lista = reduce(lambda ac, i: i + ac, lista, 0)
print(soma_lista)

print('*'*25)

#variável ac - pegando o produto P - laco - dicionario - incia o ac em zero
soma_precos = reduce(lambda ac, p: p['preco'] + ac, produtos, 0)
print(soma_precos)

soma_precos = reduce(lambda ac, p: p['preco'] + ac, produtos, 0)
print(f'media precos:{soma_precos / len(produtos)}')


print('*'*25)


#variável ac - pegando o pessoa P - laco - dicionario - incia o ac em zero
soma_idade = reduce(lambda ac, p: p['idade'] + ac, pessoas, 0)
print(soma_idade)
print(f'media idade:{soma_idade / len(pessoas)}')