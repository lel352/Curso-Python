# Operação ternária em Python

logger = True

if logger:
    msg = 'Logado'
else:
    msg = 'Precisa logar'

print(msg)
# começa com a opção verdadeira depois vem para falsa
msg2 = 'Logado' if logger else 'Precisa logar.'
print(msg2)

idade = input('Idade: ')
if not idade.isnumeric():
    print('idade precisar ser números!!')
else:
    idade = int(idade)
    maior = (idade >= 18)
    msg3 = 'Pode Acessar' if maior else 'Não pode acessar'
    print(msg3)

