# Herança múltipla

class A:
    def falar(self):
        print('Falando ... Estou em A.')


class B(A):
    def falar(self):
        print('Falando ... Estou em B.')


class C(A):
    def falar(self):
        print('Falando ... Estou em C.')


class D(B, C):  # Herda de duas classes, Herança múltipla
    pass


# Diamante - o Python busca na própria classe depois procura esquerda para direita assim, classes Pais ele procura me B se não achar procura em C, caso não achar pega em A os métods e atributos
d = D()
d.falar()

print('*'*25)

from aulapythonpoo.aula12.smartphone import Smartphone


smartphone = Smartphone('Pocophone f1')
smartphone.conectar()
smartphone.desligar()
smartphone.ligar()
smartphone.conectar()
smartphone.conectar()
smartphone.conectar()
smartphone.desligar()
smartphone.conectar()
smartphone.desconectar()