class Escritor:
    def __init__(self, nome):
        self.__nome = nome
        self.__ferramenta = None


    @property
    def nome(self):
        return self.__nome


    @property
    def ferramenta(self):
        return self.__ferramenta

    @ferramenta.setter
    def ferramenta(self, ferramenta):
        self.__ferramenta = ferramenta


    @nome.setter
    def nome(self, nome):
        self.__nome = nome


class Caneta:
    def __init__(self, marca):
        self.__marca = marca

    @property
    def marca(self):
        return self.__marca

    @marca.setter
    def marca(self, marca):
        self.__marca = marca

    def escrever(self):
        print('Caneta está escrevendo...')


class MaquinaDeEscrever:
    def escrever(self):
        print('Máquina está escrevendo...')