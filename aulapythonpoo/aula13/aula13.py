"""
Classe Abstrata

Não é instanciada
Pode ter métodos concretos e abstratos

Método contreto é aquele que apresenta corpo de programação
método abstrato não apresenta corpo de programação, mas é obrigado os filhos criarem esse método.
"""

from abc import ABC, abstractmethod # decorador abstractmethod

# colocando um método abstrato, faz com que a classe não possa ser instanciada.
class A(ABC):
    @abstractmethod
    def falar(self):
        pass


class B(A):
    def falar(self):
        print('Falando... B..')

# a = A()  Não pode porque A é classe abstrata
b = B()
b.falar()

print('*'*25)

from aulapythonpoo.aula13.classes.contapoupanca import ContaPoupanca
from aulapythonpoo.aula13.classes.contacorrente import ContaCorrente

cp = ContaPoupanca(1111, 2222, 0)
cp.depositar(10)
cp.sacar(5)
cp.sacar(5)
cp.sacar(1)

print('*'*25)

cc = ContaCorrente(agencia=1111, conta=33333, saldo=0, limite=500)
cc.depositar(100)
cc.sacar(250)
cc.sacar(500)
cc.depositar(1000)