# Map

from dados import produtos, pessoas, lista

print(lista)

nova_lista = list(map(lambda x: x * 2, lista))  # map retorna um interavel
print(nova_lista)

# mesma coisa só que com List Comprehension
nova_lista2 = [x * 2 for x in lista]
print(nova_lista2)

print('*'*25)

for produto in produtos:
    print(produto)

precos = map(lambda p: p['preco'], produtos)
for preco in precos:
    print(preco)


def aumenta_preco(p):
    p['preco'] = round(p['preco'] * 1.05, 2)
    return p


novos_produtos = map(aumenta_preco, produtos)

for produto in novos_produtos:
    print(produto)



print('*'*25)




for pessoa in pessoas:
    print(pessoa)


def aumenta_idade(p):
    p['nova_idade'] = round(p['idade'] * 1.20)
    return p


nomes = map(aumenta_idade, pessoas)

for pessoa in nomes:
    print(pessoa)


