# Aula 15 - Criando Exceções

class TaErradoError(Exception):
    pass

def testar():
    raise TaErradoError('Errado!')


try:
    testar()
except TaErradoError as error:
    print(f'Erro: {error}')
