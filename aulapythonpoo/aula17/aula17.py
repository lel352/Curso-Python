"""
https://rszalski.github.io/magicmethods/

Métodos mágicos - que modifica o compotamento da classe
"""

class A:
    # método que construi a classe;
    def __new__(cls, *args, **kwargs):
        # toda classe herda da classe object

        cls.nome = 'Luiz'

        # criar uma classe que só poder ser instância uma vez
        if not hasattr(cls, '_jaexiste'):
            cls._jaexiste = object.__new__(cls)

        return cls._jaexiste
        '''
        def haha(*args, **kwargs):
            print('fala oi')

        cls.haha = haha

        print('Eu sou o new')
        cls.nome = 'Luiz'
        return super().__new__(cls)
        '''
    # executado quando instância a classe;
    # parece o método construtor mas não é
    def __init__(self):
        print('Eu sou o INIT')



a = A()
b = A()
c = A()
print(a == b)
print(a.nome)
b.nome = 'bbb'
print(a.nome)
c.nome = 'ccc'
print(a.nome)
print(id(a), id(b), id(c))
# a.haha()

print('*'*25)

class B:
    def __init__(self):
        print('Eu sou o INIT')

    # faz a classe se comportar como um função
    def __call__(self, *args, **kwargs):
        print(args)
        print(kwargs)
        resultado =  1
        for i in args:
            resultado *= i
        return resultado

    def fala_oi(self):
        print('Oi')

    # toda vez que configurar um atributo novo ele vai ser chamado
    def __setattr__(self, key, value):
        if key == 'nome':
            valor = 'Não poder modificar nome'
        else:
            valor = value
        self.__dict__[key] = valor  # configurando o atributo para ele exister na classe
        print(key, value)

    # não é recomendado usar, pois nem sempre é chamado
    def __del__(self):
        print('Objeto Coletado')

    # toda vez que usar a classe como uma string
    def __str__(self):
        return "Essa é a classe B criada para tal coisa <class 'B' >"

    def __len__(self):
        return 55


b = B()
b(1, 2, 3, 4, 5, nome='luiz')
variavel = b(1, 2, 10, 6) # quando chmar a classe de forma como uma função ela muda seu comportamento
# no mais ela continuando sendo um classe
print(variavel)
b.fala_oi()

b.nome = 'Luiz'
print(b.nome)
b.teste = 'sadjahsd'
print(b.teste)
print(b)
print(len(b))

