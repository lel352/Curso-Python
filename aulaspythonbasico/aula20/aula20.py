'''
Aula 20 - For in - Estrutura de repetição em Python

For in
Iterando Strings com for in
Função range(start=0, stop, step=1)
'''

texto = 'Python'

for n, letra in enumerate(texto):
    print(n, letra)

print('*'*50)

for letra in texto:
    print(letra)

print('*'*50)

for numero in range(10):  # inicia no zero e termina no 10(sem colocar o 10) assim vai de 0 a 9
    print(numero)

print('*'*50)

for numero in range(5, 10, 2):  # inicia no zero e termina no 10(sem colocar o 10) assim vai de 0 a 9, o final é o passo de 2 em 2
    print(numero)

print('*'*50)

for numero in range(10): # inicia no zero e termina no 10(sem colocar o 10) assim vai de 0 a 9
    print(numero)

print('*'*50)

for numero in range(20, 10, -1):  # para fazer ao contrario tem que colocar o step como negativo, stop nunca é incluido
    print(numero)

print('*'*50)
nova_string = ''

for letra in texto:
    if letra == 't':
        nova_string += 'T'
    elif letra == 'h':
        nova_string += 'H'
    elif letra == 'y':
        continue
    elif letra == 'o':
        break
    else:
        nova_string += letra

print(nova_string)


