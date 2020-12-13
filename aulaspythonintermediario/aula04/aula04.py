# Funções (def) em Python - Parte 4 - Escopos

# escopo global assesivel em qualquer local do código
variavel = 'valor'
variavel2 = 'valor2'

print(variavel)
print(variavel2)

def func():
    print(variavel)



"""
Não se consegue alterar uma variável goblal de forma implícita, é preciso ser explicito 
usando o termo global
ex: global variavel
Não é uma boa prática de programação 
"""


def func2():
    # "varivel" é uma nova variável criada dentro do escopo dessa função(func2), somente essa função(func2) tem acesso a ela.
    variavel = 'Outro Valor'
    global variavel2  # selecionando a variável globral
    variavel2 = 'outro valor 2'
    print(variavel)
    print(variavel2)



func()
func2()

print(variavel)
print(variavel2)


def func3():
    var = 'a'
    # variável somente local, somente acessível dentro dessa função
    print(var)



