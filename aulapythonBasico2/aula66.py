"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10
Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0
Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta
O primeiro dígito do CPF é 7
"""
import string

# cpf = input('Digute um cpf: ')
cpf = '746.824.890-70'
cpf = cpf.translate(str.maketrans('', '', string.punctuation))
print(cpf)

soma = 0
multiplicador = 10

for i in cpf[:-2]:
    soma += (multiplicador * int(i)) 
    multiplicador -= 1

resultado = soma * 10

resto = resultado % 11
digitoVerificador1 = resto if resto < 9 else 0

digitofinais = cpf[-2:]
if int(digitofinais[0]) == digitoVerificador1:
    print('cpf válido !')
else: 
    print('cpf inválido !')    
