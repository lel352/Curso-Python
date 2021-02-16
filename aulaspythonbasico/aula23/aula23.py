'''
Aula 23 - Split, Join e Enumerate em Python

Split, Join, Enumarate em Python
* Split - Dividir um String # Str
* Join - Juntar uma lista # Str
* Enumerate - Enumerar elementos da list # list
'''

string = "O Brasil é o pais do futebol, o Brasil é Penta. o o o"
lista1 = string.split(' ')  # Usando o espaço para dividir a string em uma lista
print(lista1)
lista2 = string.split(',')  # virgula o espaço para dividir a string em uma lista
print(lista2)

for valor in lista1:
    print(f'A palavra {valor} apareceu {lista1.count(valor)}x na frase')


palavra = ''
contagem = 0
for valor in lista1:
    qtd_vezes = lista1.count(valor)
    if qtd_vezes > contagem:
        contagem = qtd_vezes
        palavra = valor


print(f'A palavras que aparece mais vezes é "{palavra}" ({contagem}x)')

for valor in lista2:
    print(valor.strip())  # remove os espaco do inicio e fim



# Join transforma uma lista em uma string
string = 'Brasil é penta.'
lista = string.split(' ')
print(lista)
string2 = ','.join(lista)  # juntando os elementos da lista separando eles com a virgula
print(string2)

# função enumarate usa tuplas
for v1, v2 in enumerate(lista):
    print(f'Indice: {v1}  valor: {v2}')


lista3 = [[1, 2], [3, 4], [5, 6]]
for v in lista3:
    print(v[0])

# mostrar como o enumarate funciona
lista4 = [[0, 'Luiz'], [1, 'João'], [3, 'Maria']]
for indice, nome in lista4:
    print(indice, nome)


lista5 = ['Luiz', 'João', 'Maria']
for indice, nome in enumerate(lista5):
    print(indice, nome)
    
n1, n2, n3 = lista5  # Desempacotamento
print(n1)
print(n2)
print(n3)

print('*'*20)
# Enumerate - Enumerear elementos da lista # list

lista = [
    ['Edu', 'João', 'Luiz'],
    ['Maria', 'Carla', 'Joana'],
    ['Lucas', 'Marcia', 'Helena']
]

print(lista[2])
print(lista[1][2])  # Joana

# enumera os objetos
enumerada = list(enumerate(lista))  # objeto enumerate  - elemento interado
print(enumerada)
print(enumerada[0][1])
print(enumerada[0][1][2])  # Luiz

for v1, v2 in enumerate(lista, 50):  # iniciar  o numeracao com numero 50
    print(v1, v2)
