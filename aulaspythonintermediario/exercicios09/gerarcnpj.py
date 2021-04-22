import re
from random import randint

REGRESSIVOS = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]


def removerCaracter(texto):
    return re.sub(r'[^0-9]', '', texto)


def somaDigito(cnpj, listaValoresCalculo):
    soma = 0
    for indice, regressivo in enumerate(listaValoresCalculo):
        soma += (int(cnpj[indice]) * regressivo)
    return soma


def retornaDigito(soma):
    digito = (11 - (soma % 11))
    if digito > 9:
        digito = 0
    return digito


def boSequencia(cnpj):
    sequencia = cnpj[0] * len(cnpj)
    if sequencia == cnpj:
        return True
    return False


def validaCalculaDigito(digitoValidos, numeroCnpj):
    for i in range(1, 3):
        if not validaCalculoDigito(i, digitoValidos, numeroCnpj):
            return False
    return True


def calculaDigito(digito, numeroCnpj):
    if digito == 1:
        regressivo = REGRESSIVOS[1::1]
    elif digito == 2:
        regressivo = REGRESSIVOS
    else:
        return None
    soma = somaDigito(numeroCnpj, regressivo)
    resultadoDigito = retornaDigito(soma)
    return resultadoDigito


def validaCalculoDigito(digito, digitoValidos, numeroCnpj):
    resultadoDigito = calculaDigito(digito, numeroCnpj)
    if resultadoDigito != int(digitoValidos[digito - 1]):
        return False
    return True


def validaCNPJ(cnpj):
    numeroCnpj = removerCaracter(cnpj)

    try:
        if len(numeroCnpj) < 14:
            return False

        if boSequencia(numeroCnpj):
            return False

        digitoValidos = numeroCnpj[-2::1]

        if not validaCalculaDigito(digitoValidos, numeroCnpj):
            return False

        return True
    except:
        return False  # print('CNPJ inválido !!!')


def formataCNPJ(cnpj):
    novoCnpj = removerCaracter(cnpj)
    novoCnpj = f'{novoCnpj[:2]}.{novoCnpj[2:5]}.{novoCnpj[5:8]}/{novoCnpj[8:12]}-{novoCnpj[12:14]}'
    return novoCnpj


def gerarCNPJ():
    primeiroDigito = randint(0, 9)
    segundoDigito = randint(0, 9)
    segundoBloco = randint(100, 999)
    terceiroBloco = randint(100, 999)
    quartobloco = '0001'

    inicioCNPJ = f'{primeiroDigito}{segundoDigito}{segundoBloco}{terceiroBloco}{quartobloco}'
    digito1 = f'{calculaDigito(1, inicioCNPJ+"00")}'
    auxiliar = f'{inicioCNPJ}{digito1}0'
    digito2 = f'{calculaDigito(2, auxiliar)}'
    novoCNPJ = f'{inicioCNPJ}{digito1}{digito2}'


    return formataCNPJ(novoCNPJ)


