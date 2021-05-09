class Pessoa:
    ano_atual = 2019  # Atributo de classe

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):  # Método de instância, precisa de uma instância.
        print(self.ano_atual - self.idade)

    @classmethod # criando um método de classe, precisa de uma classe.
    def por_ano_nascimento(cls, nome, ano_nascimento):
        # variável do método
        idade = cls.ano_atual - ano_nascimento
        return cls(nome, idade)


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