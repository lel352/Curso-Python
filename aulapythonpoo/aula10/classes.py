class Pessoa: # super classe
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.nome_classe = self.__class__.__name__


    def falar(self):
        print(f'{self.nome_classe} Falando...')


# Cliente herda de Pessoa
class Cliente(Pessoa): #sub Classe
    def comprar(self):
        print(f'{self.nome_classe} comprando...')


class Aluno(Pessoa): #sub Classe
    def estudar(self):
        print(f'{self.nome_classe} estudando...')
