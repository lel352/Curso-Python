# Trocando o valor entre variáveis em Python

x = 10
y = 'Luiz'
print(f'x={x} e y={y}')
# trocando valores
z = x
x = y
y = z
print(f'x={x} e y={y}')

x = 10
y = 'Luiz'
print(f'x={x} e y={y}')
# como invertar no Python os valores
y, x = x, y
print(f'x={x} e y={y}')

x = 10
y = 'Luiz'
z = 'Otávio'
print(f'x={x} e y={y} e z={z}')
# como invertar no Python os valores
y, x, z = x, z, y
print(f'x={x} e y={y} e z={z}')

