# Aula 26 - Criando, lendo, escrevendo e apagando arquivos

# forma básica

import os
import json

file = open('abc.txt', 'w+')
file.write('linha 1\n')
file.write('linha 2\n')
file.write('linha 3\n')

print('Lendo Linha')
file.seek(0, 0)  # mandando começo do arquivo
print(file.read())
print('#'*25)
file.seek(0, 0)  # mandando começo do arquivo

print(file.readline(), end='')  # lendo linha por linha
print(file.readline(), end='')  # lendo linha por linha
print(file.readline(), end='')  # lendo linha por linha

print('#'*25)
file.seek(0, 0)
print(file.readlines())

print('#'*25)
file.seek(0, 0)
for linha in file.readlines():
    print(linha, end='')

print('#'*25)
file.seek(0, 0)
for linha in file.readlines():
    print(linha, end='')

file.close()

print('*'*25)

try:
    file = open('abc2.txt', 'w+')
    file.write('linha')
    file.seek(0)
    print(file.read())
finally:
    file.close()

print('*'*25)

# Forma comum em python


# não precisa fechar o arquivo o generador fecha sozinho
with open('abc3.txt', 'w+') as file:
    file.write('linha 1 \n')
    file.write('linha 2 \n')
    file.write('linha 3 \n')

    file.seek(0)
    print(file.read())

print('*'*25)

with open('abc3.txt', 'r') as file:
    print(file.read())


print('*'*25)

# a append não apaga dados anteriores
with open('abc3.txt', 'a+') as file:
    file.write('outra linha')
    file.seek(0)
    print(file.read())

print('*'*25)

with open('abc3.txt', 'r') as file:
    print(file.read())


os.remove('abc.txt')


print('*'*25)

d1 = {
    'Pessoa 1': {
        'nome': 'Luiz',
        'idade': 25,
    },
    'Pessoa 2': {
        'nome': 'Rose',
        'idade': 30,
    }
}


d1_json = json.dumps(d1, indent=True)
print(d1_json)

with open('abc.json', 'w+') as file:
    file.write(d1_json)


