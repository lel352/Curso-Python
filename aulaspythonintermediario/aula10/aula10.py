#  List Comprehension em Python
l1 = [1, 2, 3, 4, 5, 6, 7, 8]
l2 = [variavel for variavel in l1]
print(l2)


l3 = [v * 2 for v in l1]
print(l3)

l4 = [(v, v2) for v in l1 for v2 in range(3)]
print(l4)

l1 = ['luiz', 'Mauro', 'Maria']
l5 = [v.replace('a', '@').upper() for v in l1]
print(l5)


tupla = (
    ('chave', 'Valor'),
    ('chave2', 'Valor2'),
)

l6 = [(y, x) for x, y in tupla]
print(l6)

l7 = list(range(100))
l8 = [v for v in l7 if v % 2 == 0]  # pegando todo os número divisíveis por 2
print(l8)
l9 = [v for v in l7 if v % 3 == 0 if v % 8 == 2]  # pegando todo os número divisíveis por 3 e 8
print(l9)
l10 = [v if v % 3 == 0 else 0 for v in l7]
print(l10)
l10 = [v if v % 3 == 0 and v % 8 == 0 else 0 for v in l7]
print(l10)