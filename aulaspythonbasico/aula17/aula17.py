# Aula 17 - While - estrutura de repetição em Python

# Enquanto a condição for vedadeira vai ser feitas ações dentro do While

x = 0
while x <= 10:
    print(x)
    x += 1  # x = x + 1

print('Acabou')

x = 0
while x <= 10:
    if x == 3:
       x += 1
       continue  # pula automaticamente para o próximo loop
    print(x)
    x += 1

print('Acabou')

x = 0
while x <= 10:
    if x == 3:
       x += 1
       break  # Sai do loop
    print(x)
    x += 1

print('Acabou')


x = 0  # coluna
y = 0  # linha
while x < 10:
    y = 0
    while y < 5:
        print(f'{x},{y}')
        y += 1

    x += 1


print('Acabou! ')

while True:
    print()
    num_1 = input('Digite numero 1: ')
    num_2 = input('Digite numero 2: ')
    operador = input('Digite um operador: ')


    if not num_1.isnumeric() or not num_2.isnumeric():
        print('Numeros invalidos ... ')
        continue

    num_1 = int(num_1)
    num_2 = int(num_2)

    if operador == '+':
        print(num_1 + num_2)
    elif operador == '-':
        print(num_1 - num_2)
    elif operador == '/':
        print(num_1 / num_2)
    elif operador == '*':
        print(num_1 * num_2)
    else:
        print('Operador inválido !!! ')

    sair = input('Deseja Sair ? [s] ou [n] ')
    if sair.upper() == 'S':
        break


print('Acabou')


