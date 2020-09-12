# Entrada de dados

nome = input(f"Qual o seu nome? ")
idade = input(f'Qual sua idade? ')

ano_nascimento = 2020 - int(idade)

print(f'\nSeu nome {nome} e o tipo da variável é {type(nome)}.')
print(f'{nome} tem {idade} anos. Nasceu em {ano_nascimento}.')

numero1 = int(input('Digite número 1: '))
numero2 = int(input('Digite número 2: '))
print(f'{numero1} + {numero2} = {numero1+numero2}')
