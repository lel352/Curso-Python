"""
Iterando strings com while
"""
#       01234567890123
nome = 'Leandro Sartor'  # Iteráveis
#       43210987654321
tamanho_nome = len(nome)
print(nome)
print(tamanho_nome)
print(nome[3])

nova_string = ''
nova_string = '*L*e*a*n*d*r*o* *S*a*r*t*o*r'

novo_nome = ''
indice  = 0
while indice < tamanho_nome:
    novo_nome += f'*{nome[indice]}'
    indice += 1

novo_nome += '*'
print(novo_nome)