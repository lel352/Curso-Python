# python é case sensitive
print(123456)
print('nome 1', 'nome 2')  # ele adiciona por padrão espaço entre nome 1 e nome 2, são argumentos passados para funcão print
print('nome 1', 'nome 2', sep='-')  # dizendo para função usar o '-' como separador dos temos.
print('nome 1', 'e', 'nome 2', sep='-', end='')  # com end='' ele não quebra linha, o que colocar no 'end' ele coloca no final do print
print('nome 1', 'e', 'nome 2', sep='-', end='*')  # no final do print vai ter um '*'
print('\n cpf')
print('123', '324', '534', sep='.', end='-')
print('12')
