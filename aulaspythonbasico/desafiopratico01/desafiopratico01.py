# Desafio Prático 01
from datetime import datetime
nome = 'Luiz'
idade = 33
altura = 1.80
peso = 80
ano_atual = datetime.now().year

ano_nascimento = ano_atual - idade
imc = peso / altura ** 2

print(f'{nome} tem {idade} anos, {altura} de altura e pesa {peso}kg.')
print(f'O IMC do {nome} é {imc:.2f}')
print(f'{nome} nasceu em {ano_nascimento}.')
