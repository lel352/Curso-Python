"""
Polimorfismo é o principio que permite que classes derivadas de uma mesma superclasse,
tenha métodos iguias(de mesma assinatura) mas com comportamentos diferentes.
Mesma Assinatura = Mesma quantidade e tipo de parâmetros
Python só tem polimorfismo de sobreposição
"""

from abc import ABC, abstractmethod

class A(ABC):
    @abstractmethod
    def fala(self, msg): pass


class B(A):
    def fala(self, msg):
        print(f'B está falando {msg}')

class C(A):
    def fala(self, msg):
        print(f'C está falando {msg}')


b = B()
c = C()

b.fala('Um Assunto')
c.fala('Outro Assunto')



