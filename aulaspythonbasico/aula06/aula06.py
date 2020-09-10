"""
Variáveis
* são de tipagem dinâmicas

* Iniciar sempre com letras
* pode conter números
* separar com '_' para nomes compostos ex data_atual
* letras mínusculas

= operador de atribuição
"""

nome = 'teste'
idade = 30
altura = 1.75
e_maior = idade > 18
peso = 70

print('Nome: ', nome)
print('Idade: ', idade)
print('Altura:', altura)
print('Peso: ', peso)
print('É maior:', e_maior)

print('Idade * Altura: ', idade * altura)

imc = peso / altura ** 2
print(nome, 'tem', idade, 'anos de idade e seu imc é', imc)
