arquivo = open('abc.txt', 'w')
arquivo.write('Alguma coisa')
arquivo.close()  # é bom sempre fechar o arquivo.

# gerenciador de contexto
with open('abc.txt', 'w') as arquivo:
    arquivo.write('Alguma coisa') # não preciso do close, ele faz isso sozinho


class Arquivo:
    def __init__(self, arquivo, modo):
        print('Entrou No INIT')
        self.arquivo = open(arquivo, modo)

    def __enter__(self):
        print('Retornando Arquivo')
        return self.arquivo

    def __exit__(self, exc_type, exc_val, exc_tb):
        #  exc_type, exc_val, exc_tb Só executado se aparecer uma exceção
        #  exc_type, Tipo da exceção
        #  exc_val, Valor que ta trabalhando - exceção
        #  exc_tb, traceback da exceção
        # seu eu trataar as exceções e devo retornar true return True
        print('Fechando arquivo')
        self.arquivo.close()
        # e


with Arquivo('abc.txt', 'w') as arquivo2:
    arquivo2.write('Alguma coisa pela classe')


print('*'*25)
# outra forma de criar um gerenciador de contexto

from contextlib import contextmanager

@contextmanager
def arquivoAbrir(arquivo, modo):
    try:
        print('Abrindo arquivo')
        arquivo = open(arquivo, modo)
        yield arquivo # retorna o aquivo
    finally:
        print('Fechando arquivo')
        arquivo.close()


with arquivoAbrir('abc.txt', 'w') as arquivo3:
    arquivo3.write('Linha1\n')
    arquivo3.write('Linha2\n')
    arquivo3.write('Linha3\n')

# sempre deve usar com with desses dois modo