'''
public - dentro e fora da classe,
procted - dentro e nas filhas da classe
private - somente dentro da classe.

_ privado colocar underline ela fica privado mas de uma forma simples, fraca
    Variável com um underline na frente dentro de uma classe é um atributo privado
__ privado colocar dois underline ela fica privado mas de uma forma forte
    Variável com um underline na frente dentro de uma classe é um atributo privado
'''

class BaseDeDados:
    def __init__(self):  # se comporta como um construtor
        self.__dados = {}

    @property
    def dados(self): # fazendo um metódo da classe parecer um atributo da classe
        return self.__dados

    def inserir_cliente(self, id, nome):
        if 'clientes' not in self.__dados:
            self.__dados['clientes'] = {id: nome}
        else:
            self.__dados['clientes'].update({id: nome})

    def lista_clientes(self):
        for id, nome in self.__dados['clientes'].items():
            print(id, nome)

    def apaga_cliente(self, id):
        del self.__dados['clientes'][id]

bd = BaseDeDados()
bd.inserir_cliente(1, 'Otávio')
bd.inserir_cliente(2, 'Miranda')
bd.inserir_cliente(3, 'Rose')
bd.lista_clientes()
bd.apaga_cliente(2)
print('*'*25)
bd.lista_clientes()
print('*'*25)
print(bd.dados)