from sys import path

# Formas de importar
import aula47_package.modulo
from aula47_package import modulo
from aula47_package.modulo import soma_do_modulo
# from aula47_package.modulo import *  # má pratica



# print(*path, sep='\n')
print(soma_do_modulo(1, 2))
print(aula47_package.modulo.soma_do_modulo(1, 2))
print(modulo.soma_do_modulo(1, 2))
print(variavel)
print(nova_variavel)