# Sobreprosição


from aulapythonpoo.aula11.classes import Cliente, ClienteVip


c1 = Cliente('Luiz', 45)
print(c1.nome)
c1.falar()
c1.comprar()

print('*'*25)

c2 = ClienteVip('Rose', 25, 'miranda')
print(c2.nome)
c2.falar()
c2.comprar()
