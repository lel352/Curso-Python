class A:
    vc = 123  # variável da classe, todos os objetos dessa classe teram essa variável


a1 = A()
a2 = A()

print(a1.vc)
print(a2.vc)
print(A.vc)

print('*' * 25)
A.vc = 321

print(a1.vc)
print(a2.vc)
print(A.vc)

a1.vc = 333  # criando um atributo diretamente na instância.

print(a1.vc)  # procura se tem na instância,
print(a2.vc)  # aqui não tem, ele vai e pega na classe,
print(A.vc)

print(a1.__dict__)
print(a2.__dict__)
print(A.__dict__)

print('*' * 25)


class B:
    vc = 123  # variável da classe, todos os objetos dessa classe teram essa variável

    def __init__(self):
        self.vc = 777


b1 = B()
b2 = B()

print(b1.vc)
print(b2.vc)
print(B.vc)

print('*' * 25)
B.vc = 321

print(b1.vc)
print(b2.vc)
print(B.vc)

b1.vc = 333

print(b1.vc)  # procura se tem na instância,
print(b2.vc)  # aqui não tem, ele vai e pega na classe,
print(B.vc)

print(b1.__dict__)
print(b2.__dict__)
print(B.__dict__)
