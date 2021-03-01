# Módulos padrão do Python
# Módulos são arquivos .py (em contém código python) e servem para expandir
# as funcionalidades padrão da linguagem.
# veja todos os módulos padrão do python: https://docs.python.org/3/py-modindex.html
# import sys # impotando o módulo inteiro
# print(sys.platform)

from sys import platform as so  # colocquei apelido
from random import randint, random
# from random import * uma form de importar tudo de um modulo

print(so)


for i in range(10):
    print(randint(0, 10))


def randint(*args):  # pode sobrescrever
    return 'hahaha'


for i in range(10):
    print(randint(0, 10))


print(random())  # numero entre 0 e 1, com ponto flutuante
