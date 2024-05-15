class Pesssoa:
    ano_atual = 2024  # atributo da classe

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        # self.ano_atual Self busca primeiro a instancia depois na classe
        return Pesssoa.ano_atual - self.idade


p1 = Pesssoa('Jose', 35)
p2 = Pesssoa('Marcia', 15)
print(Pesssoa.ano_atual)
Pesssoa.ano_atual = 1  # esta atrelado ao mode assim, muda em todas as intancias
print(p1.get_ano_nascimento())
print(p2.get_ano_nascimento())
