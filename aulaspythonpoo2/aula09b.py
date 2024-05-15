import json

from aula09a import Pessoa, CAMINHO_ARQUIVO, salvar_json


def ler_json():
    with open(CAMINHO_ARQUIVO, 'r') as arquivo:
        dic_pessoas = json.load(arquivo)
        p1 = Pessoa(**dic_pessoas[0])
        p2 = Pessoa(**dic_pessoas[1])
        p3 = Pessoa(**dic_pessoas[2])

        print(vars(p1))
        print(vars(p2))
        print(vars(p3))


ler_json()
