"""
Associação:
 - Composição - Uma classe é dona dos objetos de outra classe, assim se a classe for apagada a outra também é
"""

from aulapythonpoo.aula09.classes import Cliente

cliente1 = Cliente('Luiz', 32)
cliente1.insere_endereco('Belo Horizonte', 'MG')
print(cliente1.nome)
cliente1.lista_ederecos()
print()
del cliente1
print()
cliente2 = Cliente('Maria', 55)
cliente2.insere_endereco('Salvador', 'BA')
cliente2.insere_endereco('Rio de Janeiro', 'RJ')
print(cliente2.nome)
cliente2.lista_ederecos()
print()

cliente3 = Cliente('João', 19)
cliente3.insere_endereco('São Paulo', 'SP')
print(cliente3.nome)
cliente3.lista_ederecos()
print('############################')
