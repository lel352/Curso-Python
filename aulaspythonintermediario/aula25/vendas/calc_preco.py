
from aulaspythonintermediario.aula25.vendas.formata import preco

def aumenta(valor, porcentage, formata=False):
    r = valor + (valor * (porcentage / 100))
    if formata:
        return preco.real(r)
    return r

def reducao(valor, porcentage, formata=False):
    r = valor - (valor * (porcentage / 100))
    if formata:
        return preco.real(r)
    return r