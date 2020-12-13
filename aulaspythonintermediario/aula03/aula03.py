# Funções (def)  em Python - *args **Kwargs -

# uma vez que da um valor padrão para um argumento os próximos precisam de valor padrão(defaul)
def func(a1, a2, a3, a4, a5, nome=None, a6=None):
    print(a1, a2, a3, a4, a5, nome)
    return nome, a6


var = func(1, 2, 3, 4, 5, nome='A', a6='6')
print(var[0], var[1])


def func2(*args):  # permite gerar varios Parâmetros(que é uma tupla)
    print('-------------')
    print(args)
    print(args[0])
    print(args[-1])
    print(len(args))
    for v in args:
        print(v)

    args = list(args)  # transformado args em uma lista
    args = 0
    print(args)
    print('-------------')


"""
lista = [1, 2, 3, 4, 5, 6]
print(*lista)  # desempacotando a lista.
"""

func2(1, 2, 3, 4, 5)


def func3(*args):  # permite gerar varios Parâmetros(que é uma tupla)
    print(args)
    print('-------------')


lista = [1, 2, 3, 4, 5, 6]
func3(*lista)  # preciso desempacotar senão ele vai colocar toda a lista no primeiro índice da tupla
func3(lista)


# **kwargs - Argumentos nomeados entram nesse Dicionário
def func4(*args, **kwargs):
    print(args)
    print(kwargs)

    # duas formas de acessar o valor
    print(kwargs['nome'], kwargs['sobrenome'])
    nome = kwargs.get('nome')
    print(nome)
    idade = kwargs.get('idade')
    if idade is not None:
       print(idade)
    else:
        print('idade não informado !!')
    print('-------------')


# preciso desempacotar senão ele vai colocar toda a lista no primeiro índice da tupla
func4(*lista, nome='Leandro', sobrenome='Sartor')
