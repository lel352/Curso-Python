"""
Calculo do segundo dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF,
MAIS O PRIMEIRO DIGITO,
multiplicando cada um dos valores por uma
contagem regressiva começando de 11
Ex.:  746.824.890-70 (7468248907)
   11 10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0  7 <-- PRIMEIRO DIGITO
   77 40 54 64 14 24 40 36  0 14
Somar todos os resultados:
77+40+54+64+14+24+40+36+0+14 = 363
Multiplicar o resultado anterior por 10
363 * 10 = 3630
Obter o resto da divisão da conta anterior por 11
3630 % 11 = 0
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta
O segundo dígito do CPF é 0
"""

import string

cpf = '746.824.890-70'
# cpf = input('Digute um cpf: ')
cpf = cpf.translate(str.maketrans('', '', string.punctuation))

soma = 0
multiplicador = 10
nove_digitos = cpf[:-2]

for i in nove_digitos:
    soma += (multiplicador * int(i)) 
    multiplicador -= 1

resultado_digito = soma * 10

resto = resultado_digito % 11
digito_1 = resto if resto < 9 else 0

dez_digitos = nove_digitos + str(digito_1)

soma = 0
multiplicador = 11

for i in dez_digitos:
    soma += (multiplicador * int(i)) 
    multiplicador -= 1

resultado_digito = soma * 10

resto = resultado_digito % 11
digito_2 = resto if resto < 9 else 0

digitos = str(digito_1) + str(digito_2)

digitos_verificador = cpf[-2:]

if digitos_verificador == digitos:
    print('cpf válido')
else:     
    print('cpf inválido')