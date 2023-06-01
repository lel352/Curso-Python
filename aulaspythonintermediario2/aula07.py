"""
args - Argumentos não nomeados
* - *args (empacotamento e desempacotamento)
"""
# Lembre-te de desempacotamento
x, y, *resto = 1, 2, 3, 4
print(x, y, resto)

# def soma(x, y):
#     return x + y

# print(1, 2, 3, 4, 5)

def soma(*args):
    # print(args, type(args)) # Tupla
    total = 0
    for numero in args:
        total += numero
    return total


soma_1 = soma(1, 2, 3, 4, 5)
print(soma_1)

numeros = 1, 2, 3, 4, 5, 6, 7, 78, 10 #Tupla
outra_soma = soma(*numeros) # desempacotamento da tupla
print(outra_soma)

print(sum(numeros))
print(*numeros)