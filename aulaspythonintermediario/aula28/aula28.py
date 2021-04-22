# Funções decoradoras e decoradores

def fala_oi():
    print('oi')


fala_oi()

variavel = fala_oi  # variavel ser igual a função, sem o parêntese ela não executa
variavel()
print(type(variavel))

print('*'*25)

def master():
    def slave():
        print('oi')
    slave()
    return slave

master()
variavel = master()
variavel()
print(type(variavel))

print('*'*25)

def master2(funcao):
    def slave():
        print('Agora estou decorada.')
        funcao()
    return slave


master2(fala_oi)
variavel = master2(fala_oi)
variavel()
print(type(variavel))

print('*'*25)


fala_oi = master2(fala_oi)
fala_oi()


print('*'*25)

def master2(funcao):
    def slave():
        print('Agora estou decorada.')
        funcao()
    return slave

@master2
def fala_oi2():
    print('oi')

fala_oi2()

print('*'*25)


def master3(funcao):
    def slave(*args, **kwargs):
        print('Agora estou decorada.')
        funcao(*args, **kwargs)
    return slave

@master3
def outra_funcao(msg):
    print(msg)


outra_funcao('Olá, eu sou luiz. ')
print('*'*25)

from time import time, sleep

def velocida(funcao):
    def interna(*args, **kwargs):
        start_time = time()
        resultado = funcao(*args, **kwargs)
        end_time = time()
        tempo = (end_time - start_time) * 1000
        print(f'\nA função {funcao.__name__} levou {tempo:.2f}ms para executar.')
        return resultado
    return interna

@velocida
def demora():
    for i in range(10000):
        print(i, end='')
       # sleep(1)


demora()
