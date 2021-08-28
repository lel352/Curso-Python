# https://docs.python.org/3/library/json.html

"""
JavaScript Object Notation - JSON
JSON (JavaScript Object Notation) é um formato de troca de dados entre sistemas
e programas muito leve e de fácil utilização. Muito utilizado por APIs

DUMPS / Dump
######################
Python          JSON
dict	        object
list, tuple	    array
str	            string
int, float  	number
True        	true
FALSE	        False
None	        null

LOADS / Load
######################
JSON	        Python
object	        dict
array	        list
string	        str
number (int)	int
number (real)	float
true	        True
false	        False
null	        None

"""
from  aulamodulospython.aula07.dados import *
import json

lista = [1, 2, 3, 4, 5, 6]
dados_json = json.dumps(lista)
print(dados_json)
print(type(dados_json)) # classe str

# Converte um dicionário em JSON
# útil para salvar informações de qualquer tipo
dados_json = json.dumps(clientes_dicionario, indent=4)  # indentando o dados
print(dados_json)
print(type(dados_json))  # classe str

print('*'*25)
print(clientes_json)
# Converte JSON em um dicionário
# útil para carregar informações de qualquer tipo
dicionario = json.loads(clientes_json)
for chave, valor in dicionario.items():
    print(chave)
    print(valor)

print('*'*25)

# Exporta dicionário para arquivo JSON
with open('clientes.json', 'w') as arquivo:
    json.dump(clientes_dicionario, arquivo, indent=4)

# Importa string de um arquivo JSON e converte em dicionário
with open('clientes.json', 'r') as arquivo:
    dados = json.load(arquivo)

print(dados)
for chave, valor in dicionario.items():
    print(chave)
    print(valor)