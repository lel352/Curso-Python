"""
Introdução ao empacotamento e desempacotamento
"""
nomes = ['Maria', 'Helena', 'Luiz']
nome1, nome2, nome3 = nomes
print(nome1)
print(nome2)
print(nome3)

# nome1, nome2 = nomes # da erro falta variavel
# nome1, nome2, nome3, nome4 = nomes # da erro falta valores

# _ ignorando os primeiros valores
_, _, nome, *_ = ['Maria', 'Helena', 'Luiz'] # *_ pega o resto da lista, para ignorar se desejar.
print(nome)
