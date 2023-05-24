"""
Argumentos nomeados e não nomeados em funções Python
Argumento nomeado tem nome com sinal de igual
Argumento não nomeado(argumento posicional) recebe apenas o argumento (valor)
"""


def soma(x, y, z):
    # Definição
    print(f'{x=} y={y} {z=}', '|', 'x + y + z = ', x + y + z)
    # por padrão as funções retorna "None"


soma(1, 2, 3)
soma(1, z=10, y=2) # nomeou um argumento deve assim nomear todos os proximos  
soma(1, y=2, z=5)

print(1, 2, 3, sep='-')