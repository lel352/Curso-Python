"""
Fatiamento de strings
 012345678
 Olá mundo
-987654321
Fatiamento [i:f:p] [::]
Obs.: a função len retorna a qtd 
de caracteres da str
"""
variavel = 'Olá mundo'
print(variavel[4:])  # inicio: 4 até o fim
print(variavel[4:8])  # inicio 4 e para no indice 7, o 8 não é incluido
print(variavel[0:5])  # indice do 0 até o 4
print(variavel[:5])  # indice do 0 até o 4
print(variavel[-8:-2])  # indice do -3 até o -8
print(variavel[::-1])
print(len(variavel))
print(variavel[0:9:2])  # pulando de 2 em 2
print(variavel[::-1])  # Passo negatativo inverte a string
print(variavel[-1:-10:-1])  # Passo negatativo inverte a string