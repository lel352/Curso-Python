# Dicionários em Python
# chave = índice
import copy

# criando forma 1
d1 = {'chave1': 'Valor da chave'}
d1['nova_chave'] = 'Valor da nova chave'
print(d1)
print(d1['chave1'])


# criando forma 2
d2 = dict(chave1='Valor da chave', chave2='valor da outra chave')
print(d2)
print(d2['chave1'])

# chave tem que ser Única  a ultima ocorrência vai ser salva.
d3 = {'chave':'valor 1', 'chave':'valor 3', 'chave':'valor 3' }
print(d3)
print(d3['chave'])

# Somente valores imutaveis pode ser uma chave, ou seja uma tupla pode ser uma chave. uma lista não pode.
d4 = {
    'str': 'valor',
    123: 'outra valor',
    (1, 2, 3): 'Tupla'
}
print(d4[(1, 2, 3)])
if 'naoexiste' in d4: # saber se uma chave existe
    print(d1['naoexiste'])

# get não da erro se não encontra a chave somente retorna None
if d4.get('nomedachave') is not None:
   print(d4.get('nomedachave'))

d4['str'] = 'mudando o valor'
print(d4)

d4.update({'nova_chave': 'Novo_valor'})
print(d4)
#ou
d4['nova_chave2'] = 'Novo valor 2'
print(d4)

# deletar
del d4['str']
print(d4)

print(123 in d4) # ver se chave 123 existe
# ou
print('str' in d4.keys())  # ver se chave 'str existe
print('valor' in d4.values())  # ver se valor 'valor' existe
print(len(d1))  # quantos pares.


d5 = {
    'chave 1': 'valor',
    'chave 2': 'outra valor',
    'chave 3': 'Tupla'
}

print('-'*25)
print('Chave: ')
for k in d5:
    print(k)
print('-'*25)
print('Valor: ')
for v in d5.values():
    print(v)
print('-'*25)
for k in d5.items():
    print(k)
print('-'*25)
for k, v in d5.items():
    print(f'{k}: {v}')
print('-'*25)

clientes = {
    'cliente1': {
      'Nome': 'Luiz',
      'Sobrenome': 'Otavio'
    },
    'cliente2': {
        'Nome': 'Joao',
        'Sobrenome': 'Silva'
    }
}
print('-'*25)
for cliente_k, cliente_v in clientes.items():
    print(f'Exibindo {cliente_k}')
    for dados_k, dados_v in cliente_v.items():
        print(f'\t{dados_k} = {dados_v}')


print('-'*25)


d6 = {
  1: 'a',
  2: 'b',
  3: 'c'
}

# Não estou copiando mas sim referenciando os 'v' com o mesmo caminho da memória que o d6
# assim tudo que modifico em um vai aparecer no outro, mas eles tem a mesmo caminho na memória.
# não está criando o memso objeto mas ambos aponta o mesmo lugar na memória.
v = d6

print(d6)
print(v)

v[1] = 'Casa'

print(d6)
print(v)

# uma copia profunda que cria uma novo objeto
# o somente o copy gera uma copia simple que ainda pode alterar no original.
v = copy.deepcopy(d6)
print(d6)
print(v)

v[1] = 'Marca'
print(d6)
print(v)

lista = [
    ['c1', 1],
    ['c2', 2],
    ['c3', 3]
]

# como a lista tem valores par, assim pode conveter em dicionário
d7 = dict(lista)
print(d7)
print('-'*25)
tupla = (
    ['c1', 1],
    ['c2', 2],
    ['c3', 3]
)

# como a lista tem valores par, assim pode conveter em dicionário
d8 = dict(tupla)
print(d8)

# elimando a chave que desejo iliminar
d8.pop('c2')
print(d8)
# elimina o último item
d8.popitem()
print(d8)

d9 = {
  1: 'a',
  2: 'b',
  3: 'c'
}
print(d9)
# juntando dois dicionários
d8.update(d9)
print(d8)

