import re

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

def calculadigito(digitoValidos, numeroCnpj):
    for i in range(1, 3):
        if not calculadigito2(i, digitoValidos, numeroCnpj):
            return False
    return True


def calculadigito2(digito, digitoValidos, numeroCnpj):
    if digito == 1:
        regressivo = REGRESSIVOS[1::1]
    elif digito == 2:
        regressivo = REGRESSIVOS
    else:
        return False

    soma = somaDigito(numeroCnpj, regressivo)
    resultadoDigito = retornaDigito(soma)
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

        if not calculadigito(digitoValidos, numeroCnpj):
            return False

        return True
    except:
        return False #print('CNPJ inválido !!!')



