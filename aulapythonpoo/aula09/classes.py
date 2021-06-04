class Cliente:
    def __init__(self, nome, idade):
        self.__nome = nome
        self.__idade = idade
        self.enderecos = []

    @property
    def nome(self):
        return self.__nome

    @property
    def idade(self):
        return self.__idade

    def insere_endereco(self, cidada, estado): # Associação composição
        self.enderecos.append(Endereco(cidada, estado))

    def lista_ederecos(self):
        for endereco in self.enderecos:
            print(endereco.cidade, endereco.estado)

    def __del__(self):
        print(f'{self.nome} FOI APAGADO')

class Endereco:
    def __init__(self, cidade, estado):
        self.__cidade = cidade
        self.__estado = estado

    @property
    def cidade(self):
        return self.__cidade

    @property
    def estado(self):
        return self.__estado

    def __del__(self):
        print(f'{self.cidade}/{self.__estado} FOI APAGADO ')
