#  Introdução a Formatação de String

nome = 'teste'
idade = 30
altura = 1.75
e_maior = idade > 18
peso = 70
imc = peso / altura ** 2

print(nome, 'tem', idade, 'anos de idade e seu imc é', imc)
# fstring
print(f'{nome} tem {idade} anos de idade e seu imc é {imc:.2f}')
# format
print('{} tem {} anos de idade e seu imc é {:.2f}'.format(nome, idade, imc))
# print('{0} tem {1} anos de idade e seu imc é {2 :.2f}'.format(0->nome,1-> idade,2-> imc))
print('{n} tem {i} anos de idade e seu imc é {m :.2f}'.format(n=nome, i=idade, m=imc))