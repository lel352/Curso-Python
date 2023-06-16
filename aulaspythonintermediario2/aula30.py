lista = []
for x in range(3):
    for y in range(3):
        lista.append((x, y))
print(lista) 

lista = [
    (x, y)
    for x in range(3)
    for y in range(3)
]
print(lista)
print()

lista = [
    [x for y in range(3)]
    for x in range(3)
]
print(lista)
print()

lista = [
    [letra for letra in 'Leandro']
    for x in range(3)
]
print(lista)
print()


lista = [
    [(x, letra) for letra in 'Leandro']
    for x in range(2)
]

print(lista)
print()

nomes = ['luiz', 'maria', 'helena', 'joana', 'felipe']
novos_nomes = [
    f'{nome[:-1].lower()}{nome[-1].upper()}'
    for nome in nomes
]
print(novos_nomes)
print()

string = 'Otávio Miranda'
numero_de_letras = 2
nova_string = '.'.join([
    string[indice:indice + numero_de_letras]
    for indice in range(0, len(string), numero_de_letras)
])
print(nova_string)