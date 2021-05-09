from random import randint

class Pessoa:
    ano_atual = 2019  # Atributo de classe

    def __init__(self, nome, idade):
        self.nome = nome  # Atributo de instância
        self.idade = idade # Atributo de instância

    def get_ano_nascimento(self):  # Método de instância, precisa de uma instância.
        print(self.ano_atual - self.idade)

    @classmethod # criando um método de classe, precisa de uma classe.
    def por_ano_nascimento(cls, nome, ano_nascimento):
        # variável do método
        idade = cls.ano_atual - ano_nascimento
        return cls(nome, idade)

    @staticmethod # não precisa da classe e nem da instância.
    def gera_id():
        rand = randint(10000, 19999)
        return rand



p1 = Pessoa('Luiz', 32)
print(p1)
print(p1.nome, p1.idade)
p1.get_ano_nascimento()
print()
p2 = Pessoa.por_ano_nascimento('Luiz 2', 1987)
print(p2)
print(p2.nome, p2.idade)
p2.get_ano_nascimento()
p3 = p2.por_ano_nascimento('aa', 2010)
print(p3)
print(p3.nome, p3.idade)
print('-'*23)
print(Pessoa.gera_id())
print(p3.gera_id())