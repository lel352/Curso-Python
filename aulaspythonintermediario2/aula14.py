# Métodos úteis dos dicionários em Python
# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe
# copy - retorna uma cópia rasa (shallow copy)
# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro
pessoa = {
    'nome': 'Luiz Otávio',
    'sobrenome': 'Miranda',
    'idade': 900,
}

pessoa.setdefault('idade', 0) # se tiver a chave ele não faz nada.
print(f'Pessoa.idade: {pessoa["idade"]}')
print(f'len: {len(pessoa)}')
print(f'Keys: {list(pessoa.keys())}')
print(f'Values: {list(pessoa.values())}')
print(f'Item: {list(pessoa.items())}')

for chave in pessoa.keys():
     print(chave)

for valor in pessoa.values():
     print(valor)

for chave, valor in pessoa.items():
     print(chave, valor)