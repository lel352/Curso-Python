from abc import ABC, abstractmethod

class Pessoa(ABC):
    def __init__(self, nome, idade):
        self.__nome = nome
        self.__idade = idade

    @property
    def nome(self):
        return self.__nome

    @property
    def idade(self):
        return self.__idade

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @idade.setter
    def idade(self, idade):
        self.__idade = idade


class Cliente(Pessoa):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)

    def inserir_conta(self, conta):
        self.__conta = conta

    @property
    def conta(self):
        return self.__conta

    # @conta.setter
    # def conta(self, conta):
    #   self.__conta = conta

