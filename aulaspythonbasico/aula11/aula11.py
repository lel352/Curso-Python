#  Operadores lógicos + IF/ELIF/ELSE
# and, or, not, in e not in
'''
true and true  = true
true and false = false
false and true = false
false and false = false

True or True  = true
true or false = true
false or true = true
false or false = false

inverte
not true = false
not false =  true
'''

a = 2
b = 3

if b > a:
    print('B é maior que A')
else:
    print('A é maior que B')

if not b > a:
    print('B é maior que A')
else:
    print('A é maior que B')

a = ''
b = 0
if not a:  # ver se a variável tem valor
    print('preencha o valor de A')

if not b:  # ver se o valor for zero ele tente que é um bolean false (false = 0)
    print('preencha o valor de A')

nome = 'Luiz Otávio'

if 'u' in nome:
    print('Existe a letra u no seu nome')

if 'Ota' in nome:
    print('Existe a Ota no seu nome')
else:
    print('Não Existe a Ota no seu nome')

if 'Ota' not in nome:
    print('Não Existe a Ota no seu nome')
else:
    print('Existe a Ota no seu nome')


usuario = input('Usuário: ')
senha = input('Senha: ')

usarioBd = 'luiz'
senhaBd = '123456'

if usarioBd == usuario and senha == senhaBd:
    print('Logado !!!')
else:
    print('Usuário e senha inválidos! ')
