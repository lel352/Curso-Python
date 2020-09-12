# Aula 10 - Operadores relacionais + IF/ELIF/ELSE
# == > >= < <= !=

# == comparação de Igualdade, perguntando se uma coisa é igual a outra.
numero1 = 2
numero2 = 2
print(2 == 2)
print(2 == 1)
print(2 == '2')
expressao = numero1 == numero2
print(f'numero1 == numero2: {expressao}')
# > ver numero1 é 'maior que' numero 2
expressao = numero1 > numero2
print(f'numero1 > numero2: {expressao}')
# >= ver numero1 é 'maior que ou igual que' numero 2
expressao = numero1 >= numero2
print(f'numero1 >= numero2: {expressao}')
# < ver numero1 é 'menor que' numero 2
expressao = numero1 < numero2
print(f'numero1 < numero2: {expressao}')
# <= ver numero1 é 'menor que ou igual que' numero 2
expressao = numero1 <= numero2
print(f'numero1 < numero2: {expressao}')
# != ver numero1 é 'diferente' numero 2 -> Se for diferente retorna true ! simbolo de negação
expressao = numero1 != numero2
print(f'numero1 != numero2: {expressao}')
var1 = 'Luiz'
var2 = 'teste'
expressao = var1 != var2
print(f'{var1} != {var2}: {expressao}')

nome = input('Qual seu nome: ')
idade = int(input('Idade: '))

limiteMenor = 20
limiteMaior = 30

if limiteMenor <= idade <= limiteMaior: # idade >= limiteMenor and idade <= limiteMaior
    print(f'\n{nome} pode pegar o Empréstimo. ')
else:
    print(f'\n{nome} não pode pegar o Empréstimo. ')
