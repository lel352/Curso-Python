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
p1 = {
    'nome': 'Luiz',
    'sobrenome': 'Miranda',
}
print(f'nome: {p1["nome"]}')
print(f'Com get: {p1.get("nome", "Não existe")}')

nome = p1.pop('nome') # elimina a chave
print(f'pop: {nome}')

print(p1)
print()

p1 = {
    'nome': 'Luiz',
    'sobrenome': 'Miranda',
}

ultima_chave = p1.popitem()
print(f'{ultima_chave=}')
print(p1)
print()

p1.update({
     'nome': 'novo valor',
     'idade': 30,
})
# ou p1.update(nome='novo valor', idade=30)
# ou tupla = (('nome', 'novo valor'), ('idade', 30)) p1.update(tupla)
# ou lista = [['nome', 'novo valor'], ['idade', 30]] p1.update(lista)
print(p1)

