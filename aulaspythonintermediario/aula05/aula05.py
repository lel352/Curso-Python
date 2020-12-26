# Expressões lambda (funções anônimas) em Python

def funcao(arg, arg2):
    return arg * arg2;


var = funcao(2, 4)

a = lambda x, y: x * y

print(a(2, 2))


lista = [
    ['P1', 12],
    ['P2', 17],
    ['P3', 52],
    ['P4', 15],
    ['P5', 1],
    ['P6', 89]
]
print(lista)

# ordenando pelo preço
print('Sorted 1', sorted(lista, key=lambda item: item[1]))  # sorted não afeta a lista original
print('Sorted 2 reverse', sorted(lista, key=lambda item: item[1], reverse=True))  # sorted não afeta a lista original


print('Lista', lista)


lista.sort(key=lambda item: item[1])
print('sort 1', lista)

lista.sort(key=lambda item: item[1], reverse=True)
print('sort 2 reverse', lista)
