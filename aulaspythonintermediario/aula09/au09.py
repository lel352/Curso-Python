# Conjuntos em Pythons
# Set só aceita valores unicos. são valores imutaveis
# add (adiciona), update (atualiza), clear, discard.
# union | (une)
# intersection & (Todos os elementos presente nos dois sets)
# difference - (elementos apenas no set da esquerda)
# symmetric_difference ^ (Elementos que estão nos dois set, mas não em ambos)
# não respeita ordem, pode variar acada vez

# criando coma parênteses
s1 = {1, 2, 3, 5, 6, 7, 8, 9}

print(s1)
print(type(s1))
#  posso interar os valores, mas não posso acesar com indice
for v in s1:
    print(v)

print()
s2 = set()  # cria um set vazio.
s2.add(1)
s2.add(2)
print(s2)
s2.discard(2)  # apagar elemento
print(s2)

s2.update('a')
print(s2)
s2.update('python')  # vai interar cada elementos da string python
print(s2)

print()
s3 = set()
s3.update([1, 2, 3, 4, 5], {5, 6, 7, 8})
print(s3)

l1 = [1, 2, 3, 5, 5, 5, 4, 4, 3, 4, 8, 4, 5, 6, 7, 8, 9, 1, 'Luiz', 'Luiz']
print(l1)
l1 = set(l1)  # Virou um set, mas não tem mais elementos repetidos
print(l1)
l1 = list(l1)  # voltou ser uma lista, agora sem os valores duplicados

print()


s4 = {1, 2, 3, 4, 5, 7}
s5 = {1, 2, 3, 4, 5, 6}
print(f'set1 {s4}')
print(f'set2 {s5}')
s6 = s4 | s5  # União
print(f'union(União): {s6}')
s7 = s4 & s5  # intercessão o que tem de igual nos dois set (conjuntos)
print(f'intersection(intercessão): {s7}')
# diferencia dentre os set, mas só vai mostrar os elementos diferentes presente no s4, o set a esquerda do sinal
s8 = s4 - s5
print(f'difference(diferencia s1){s8}')
# diferencia dentre os set, mas só vai mostrar os elementos diferentes presente no s4, o set a esquerda do sinal
s9 = s5 - s4
print(f'difference(diferencia s2){s9}')
s10 = s4 ^ s5
# Elementos que estão no dois set mas que não estão presente nos dois ap mesmo tempo.
print(f'symmetric_difference(elementos unicos, que não estão em ambos) {s10}')


print()

l1 = ['Luiz', 'João', 'Maria']
l2 = ['Luiz', 'João', 'Maria', 'Luiz', 'João', 'Maria', 'Luiz', 'João', 'Maria', 'Luiz', 'João', 'Maria']

print(l1 == l2)

l1 = set(l1)
l2 = set(l2)

print(l1 == l2)
