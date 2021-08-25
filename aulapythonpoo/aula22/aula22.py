# SETTER = CONFIGURANDO UM VALOR (=)
# GETTER = OBTER UM VALOR (.)
class Pessoa:
    def __init__(self, nome):
        self._nome = nome

    @property
    def nome(self):
        return self._nome

    @nome.setter # para ter um setter precisa de um Get configurado
    def nome(self, nome):
        self._nome = nome

    @property
    def sobrenome(self):
        return 'DESCONHECIDO'


p1 = Pessoa('Otávio')
print(p1.nome)
print(p1.sobrenome)
