# Funções (def) em Python - Parte 2 - Return

def funcao(var):
    print(var)

'''
função sempre retorna um valor mesmo não tendo um "return" nela
'''
variavel = funcao('oi')
print(variavel)  # retorna None = Tipo de dado básico que representa algo sem algum valor.
if not variavel:
    print('Nenhum valor !!! ')

def funcao2(var):
    return var
    # ao return ser executado a função é finalizada, tudo logo após ele é ignorado
    print('Teste', var)


variavel = funcao2('oi')
print(variavel)  # retorna None = Tipo de dado básico que representa algo sem algum valor.
if variavel:
   print(variavel)
else:
   print('Nenhum valor !!! ')


def divisao(n1, n2):
    if n2 == 0:
        return

    return n1 / n2


divide = divisao(8, 2)
if divide:
    print(divide)
else:
    print('Conta inválida !!')


def dumb():
    # return 1
    # return True
    return [1, 3, 4, 4, 4]
    # pode retornar o que desejar


print(dumb(), type(dumb()))


def f(v):
    print(v)


def dumb2():
    return f  # Como não to utilizando os parenteses em f, eu estou retornando a funcao f, não executando ela.


var = dumb2()
var('E colocar o meu valor aqui')
#  var virou uma função pois o retorno de dumb2 é a função f em si
print(f == var)
print(id(var), id(f))
print(dumb2(), type(dumb2()))


def dumb3():
    return ('Leandro', 'Sartor')


var = dumb3()
print(var, type(var))  # retornou uma tupla, uma lista que não pode ser alterada.