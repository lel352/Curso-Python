# Exercício - Salve sua classe em JSON
# Salve os dados da sua classe em JSON
# e depois crie novamente as instâncias
# da classe com os dados salvos
# Faça em arquivos separados.

import json

CAMINHO_ARQUIVO = 'aula9Json.json'


class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


p1 = Pessoa('Pessoa 1', 10)
p2 = Pessoa('Pessoa 2', 20)
p3 = Pessoa('Pessoa 3', 30)

dic_pessoa = [vars(p1), vars(p2), vars(p3)]


def salvar_json(dic):
    with open(CAMINHO_ARQUIVO, 'w', encoding='utf8') as arquivo:
        json.dump(
            dic,
            arquivo,
            ensure_ascii=False,
            indent=2,
        )
    print('Salvo !!!')


if __name__ == '__main__':
    salvar_json(dic_pessoa)
