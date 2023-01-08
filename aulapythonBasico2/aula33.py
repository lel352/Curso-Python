"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

valor = input('Digite um número Inteiro: ')
try:
    numero = int(valor)
    if numero % 2 == 0:
        print(f'Valor {numero} é Par. ')
    else:
        print(f'Valor {numero} é Impar. ')
except:
    print('Valor digitado não é um valor Inteiro.')

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário
descrito, exiba a saudação apropriada. Ex.
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
hora = input('Digite uma hora: ')
try:
    numero = int(hora)
    if 0 <= numero <= 11:
        print('Bom Dia ')
    elif 12 <= numero <= 17:
        print('Boa Tarde')
    elif 18 <= numero <= 23:
        print('Boa Noite')
    else:
        print('Hora digita é inválida.')
except:
    print('Valor digitado não é uma Hora válida.')

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande".
"""

nome = input('Digite seu nome: ')
if nome:
    tamalho = len(nome)
    if tamalho <= 4:
        print(f'Nome({nome}) é Curto')
    elif 5 <= tamalho <= 6:
        print(f'Nome({nome}) é Normal')
    elif tamalho > 6:
        print(f'Nome({nome}) é Grande')
else:
    print('Nada foi digitado. ')
