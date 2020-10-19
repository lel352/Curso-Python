# Formatando valores em Python
'''
:s - Texto(Strings)
:d - Inteiros(int)
:f - números com pontos flutuantes (float)
:.(NÙMERO)f - Quantidade de casas decimais(float)
:(CARACTERE) (> ou < ou ^) (QUANTIDADE) (tipo -s, d ou f)
             > esquerda
             < direta
             ^ Centro
'''


num1 = 10
num2 = 3

divisao = num1 / num2
print('{:.2f}'.format(divisao))
print(f'{divisao:.2f}')

num1 = 1
print(f'{num1:0>10}') # 10 casas - tamanho do valor o resto é complementado com 0 a esquerda

num2 = 1150
print(f'{num2:0>10}')  # 10 casas - tamanho do valor o resto é complementado com 0 a esquerda
print(f'{num2:0<10}')  # 10 casas - tamanho do valor o resto é complementado com 0 a direta
print(f'{num2:0^10}')  # 10 casas - tamanho do valor o resto é complementado com 0 a Centralizando o número
print(f'{num2:.2f}')
print(f'{num2:0>10.2f}')

nome = 'teste';
print(f'{nome:#^50}')


nome = 'Leandro Sartor'
nome_formatado = '{:@>50}'.format(nome)
print(nome_formatado)
nome_formatado = '{:@>7}'.format(nome)
print(nome_formatado)
nome_formatado = '{n:@>15}{n:@>15}{n:@>15}'.format(n=nome)
print(nome_formatado)
nome_formatado = '{n:0<20}'.format(n=nome)
print(nome_formatado)
nome = 'Leandro'
sobrenome = 'Sartor'
nome_formatado = '{1:0<20}'.format(nome, sobrenome)
print(nome_formatado)
nome_formatado = '{0:$^50}{1:0^50}'.format(nome, sobrenome)
print(nome_formatado)
nome = nome.zfill(10) # 10 caracteres junto com o nome o resto para chegar a 10, preenxe com zero
print(nome)
nome = 'Leandro'
nome = nome.ljust(20, '#')  # Justifica a Esquerda e preenxe do resto com # dentro de 20 caracteres
print(nome)
nome = 'Leandro sartor'
print(nome.lower())  # Tudo minúsculo
print(nome.upper())  # Tudo maiúsculo
print(nome.title())  # Primeiras letras maiúsculo

