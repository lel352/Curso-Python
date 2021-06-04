class Pessoa:  # super classe
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

    def falar(self):
        print('Estou em cliente')


# Herda de Cliente, tem tudo de cliente e de pessoa
class ClienteVip(Cliente):
    def __init__(self, nome, idade, sobrenome):
        super().__init__(nome, idade)
        self.sobrenome = sobrenome
    
    
    def falar(self):  # sobreescrevendo o método falar
        Pessoa.falar(self)  # chamando o falar da classe pessoa,f forma de escolher de qual herança deseja busar o método
                            # Desse modo precisa enviar o Self
        super().falar()  # está se referindo a super classe aqui é a Cliente
        print(f'{self.nome} {self.sobrenome}')


