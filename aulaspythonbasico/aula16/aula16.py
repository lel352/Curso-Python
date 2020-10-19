# Índices e fatiamento de strings em Python
'''
Manipulando String
* String Indices
* Fatiamento de String [Inicio:Fim:Passo]
* Funções built-in len, abs, type, print, etc...
'''
#       [012345678] Positivos
texto = 'Python S2'
#      -[987654321] Negativos
print(texto[2])
print(texto[-7])


print(texto[-1])  # pega o último caracter

url = 'www.google.com.br/'
print(url[:-1])

#  pegando trechos
nova_string = texto[2:6]  # vai pegar do indice 2 ao 5 (6 não é incluido, fim não é incluido)
print(nova_string)

nova_string = texto[:6]  # Sem valor entende que é zero [:6] = [0:6]
print(nova_string)

nova_string = texto[7:]  # Sem valor entende que é final [7:] = [7:9]
print(nova_string)

nova_string = texto[-9:-3]
print(nova_string)

nova_string = texto[:-1]  # pegando do indice zero e excluindo o último caracter
print(nova_string)

# Passo Step
nova_string = texto[::2]  # do inicio até o último caracter, pulando de 2 em 2
print(nova_string)

nova_string = texto[0:6:2]  # do inicio até o 5 caracter, pulando de 2 em 2
print(nova_string)

nova_string = texto[0::3]  # do inicio até o último caracter, pulando de 3 em 3
print(nova_string)


