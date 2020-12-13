# Funções - def em Python (parte 1)

def funcao():
    print('Hello World!')


def funcao2(msg):
    print(msg)


def saudacao(msg='Olá', nome='Usuário Padrão'):  # To informando o valão default(padrão), caso não seja informado algum valor
    print(msg, nome)


def saudacao2(msg='Olá', nome='Usuário Padrão'):
    nome = nome.replace('e', '3')
    msg = msg.replace('e', '3')
    print(msg, nome)


funcao()
funcao2('Olá Mundo')
saudacao('Olá', 'Leandro')
saudacao()  # usa o valores padrão

saudacao(nome='João')  # usando os argumentos nomeados
saudacao(nome='João',msg='Oi')  # assim posso inverter a onder dos argumentos

saudacao2('Olá', 'Leandro')
saudacao2()  # usa o valores padrão
saudacao2(nome='João')  # usando os argumentos nomeados
saudacao2(nome='João',msg='Oi')  # assim posso inverter a onder dos argumentos
