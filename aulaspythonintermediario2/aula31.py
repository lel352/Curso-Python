# Dictionary Comprehension e Set Comprehension
produto = {
    'nome': 'Caneta Azul',
    'preco': 2.5,
    'categoria': 'Escritório',
}
print(produto)

dc = {
    chave: valor.upper() if isinstance(valor, str) else valor
    for chave, valor in produto.items()
    if chave != 'categoria'
}

print()
print(dc)

lista = [
    ('a', 'valor a'),
    ('b', 'valor a'),
    ('b', 'valor a'),
]
print()
print(lista)


dc = {
    chave: valor
    for chave, valor in lista
}

print()
print(dc)


s1 = {2 ** i for i in range(10)}
print(s1)