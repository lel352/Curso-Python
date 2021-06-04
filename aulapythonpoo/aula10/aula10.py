"""
Associação - Usa | Agregação - Tem | Composição - É dono | Herança - É
"""
from aulapythonpoo.aula10.classes import Pessoa, Cliente, Aluno


c1 = Cliente('Luiz', 45)
print(c1.nome)
c1.falar()
c1.comprar()


a1 = Aluno('Maria', 45)
print(a1.nome)
a1.falar()
a1.estudar()


p1 = Pessoa('João', 54)
p1.falar()
