# Aula 24 -  Desempacotamento de listas em Python

lista = ['Luiz', 'João', 'Maria', 'Marcos', 'Julia']

n1, n2, n3, n4, n5 = lista  # A quantidade variveis tem que ser igual ao quantidad de elementos

print(n2)

v1, *outraLista, ultimoLista = lista  # O restante dos valores da lista vai para uma nova lista, precisa usar '*'
# ultimoLista colocar esse variável por último após '*' na lista faz com que o ultmo valor da lista vai para ela
print(v1)
print(outraLista)
print(ultimoLista)

*outraLista2, v1, v2 = lista  # * gera uma lista, como coloquei variáveis apos ele, cada uma delas pegará os ultimos valores
print(outraLista2)
print(v1)
print(v2)


n1, n2, *_ = lista  # *_ não está se preocupando com o resto da lista, somente deseja pegar os valores inciais