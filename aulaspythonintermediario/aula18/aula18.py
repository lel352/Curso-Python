# filter - Filtrar - verdadeiro ou falso para buscar

from aulaspythonintermediario.aula17.dados import lista, produtos, pessoas

nova_lista = filter(lambda x: x > 5, lista) # retorna um interador interater
print(list(nova_lista))

# mesma coisa só que com List Comprehension
nova_lista2 = [x for x in lista if x > 5]
print(nova_lista2)

print('*'*25)


nova_lista = filter(lambda p: p['preco']> 50, produtos)
for produto in nova_lista:
    print(produto)


def filtra(p):
    if p['preco'] > 50:
        p['e_caro'] = True # não é correto mas funciona fazer isso no filter, igual no map
        return True
    return False

nova_lista = filter(filtra, produtos)
for produto in nova_lista:
    print(produto)


print('*'*25)



def filtra2(pessoa):
    if pessoa['idade'] >= 18:
        return True
    return False


nova_lista = filter(filtra2, pessoas)
for pessoa in nova_lista:
    print(pessoa)
