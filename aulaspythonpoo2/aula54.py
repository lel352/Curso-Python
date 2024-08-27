# Enum -> Enumerações
# Enumerações na programação, são usadas em ocasiões onde temos
# um determinado número de coisas para escolher.
# Enums têm membros e seus valores são constantes.
# Enums em python:
#   - são um conjunto de nomes simbólicos (membros) ligados a valores únicos
#   - podem ser iterados para retornar seus membros canônicos na ordem de
#       definição
# enum.Enum é a superclasse para suas enumerações. Mas também pode ser usada
#   diretamente (mesmo assim, Enums não são classes normais em Python).
# Você poderá usar seu Enum com type annotations, com isinstance e
# outras coisas relacionadas com tipo.
# Para obter os dados:
# membro = Classe(valor), Classe['chave']
# chave = Classe.chave.name
# valor = Classe.chave.value

import enum

DirecoesE = enum.Enum('Direcoes', ['ESQUERDA', 'DIREITA'])
print(DirecoesE(1))
print(DirecoesE(1).value)
print(DirecoesE(1).name)
print(DirecoesE['ESQUERDA'])
print(DirecoesE.ESQUERDA)
print(DirecoesE.ESQUERDA.name)
print(DirecoesE.ESQUERDA.value)


def mover(direcao: DirecoesE):
    if not isinstance(direcao, DirecoesE):
        raise ValueError('Direção não encontrada')

    print(f'Movendo para {direcao}')


mover(DirecoesE.ESQUERDA)
mover(DirecoesE.DIREITA)

print('-'*20)


class Direcoes(enum.Enum):
    ESQUERDA = 1  # enum.auto() gera numero automaticamente
    DIREITA = 2


print(Direcoes(1))
print(Direcoes(1).value)
print(Direcoes(1).name)
print(Direcoes['ESQUERDA'])
print(Direcoes.ESQUERDA)
print(Direcoes.ESQUERDA.name)
print(Direcoes.ESQUERDA.value)


def mover(direcao: Direcoes):
    if not isinstance(direcao, Direcoes):
        raise ValueError('Direção não encontrada')

    print(f'Movendo para {direcao.name} ({direcao.value})')


mover(Direcoes.ESQUERDA)
mover(Direcoes.DIREITA)
