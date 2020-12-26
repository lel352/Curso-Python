# Aula 06 - Tuplas em Python
# uma vez criada uma tupla não pode ser modificada.
t1 = (1, 2, 3, 'a', 'Teste teste')

print(t1[1])
print(t1)
for v in t1:
    print(v)

#  pode fatiar uma tupla
print(t1[2:])

# criando um tupla sem Parêntese
t2 = 1, 2, 'a', 'b'
print(t2)

# colocar um Vírgula no final cria um tupla
t3 = 1,
print(t3, type(t3))

t4 = 1, 2, 'Luiz', 4, 5
t5 = 6, 7, 8, 9, 10
t6 = t4 + t5
print(t6)

# desempacotando
n1, n2, n3, *_, n10 = t6
print(n3)
print(n10)

# repetindo o valor 5 vezes
t7 = (1, 2, 'Luiz', 4, 5) * 5
print(t7)

t8 = (1, 2, 3, 4, 5,)
t8 = list(t8)  # transformando a tupla em lista
t8[1] = 3000
print(t8)
t8 = tuple(t8)  # transformando a lista em tupla
