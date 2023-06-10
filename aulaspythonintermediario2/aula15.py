# Métodos úteis dos dicionários em Python
# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe
# copy - retorna uma cópia rasa (shallow copy) (copia rasa)
# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro
import copy

d1 = {
    'c1': 1,
    'c2': 2,
    'l1': [0, 1, 2],
}
# d2 = d1 # aponta para o mesmo dicionario na memória, assim alterar o d2 altera o d1
d2 = d1.copy() # copisa soment e que é imutável, copy não entra em subniveis, ou seja l1 tem uma list, ele não copiou ela.  

d2['c1'] = 1000
d2['l1'][1] = 999999

print(d1)
print(d2)
print()

d3 = copy.deepcopy(d1) # copia profunda assim, um não vai afetar o outro.  

d3['c1'] = 2000
d3['l1'][1] = 333333

print(d1)
print(d2)
print(d3)