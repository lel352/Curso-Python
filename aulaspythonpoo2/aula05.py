# Escopo da classe e de métodos da classe

class Animal1:
    nome = 'Leão'


print(Animal1.nome)


class Animal:
    # Escopo
    def __init__(self, nome):
        # Escopo
        self.nome = nome

        variavel = 'valor'
        print(variavel)

    def comendo(self, alimento):
        # Escopo
        return f'{self.nome} está comendo {alimento}'
        # print(variavel) nãot tem acesso

    def executar(self, *args, **kwargs):
        # Escopo
        return self.comendo(*args, **kwargs)


leao = Animal(nome='Leão')
print(leao.nome)
print(leao.comendo('carne'))
print(leao.executar('peixe'))
