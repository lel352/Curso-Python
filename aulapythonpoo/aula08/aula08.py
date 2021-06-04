"""
Associação:
de Agregação - Uma classe usa outra classe como parte de si, ela precisa dessa classe
"""

from aulapythonpoo.aula08.classes import Produto, CarrinhoDeCompras

carrinho = CarrinhoDeCompras() # pode existir sem produtos, mas não faz nada sem eles
print(carrinho)

p1 = Produto('Camiseta', 50)
p2 = Produto('Celular', 1000)
p3 = Produto('Caneta', 15)


carrinho.inserir_produto(p1)
carrinho.inserir_produto(p2)
carrinho.inserir_produto(p3)
carrinho.inserir_produto(p1)
carrinho.inserir_produto(p1)
carrinho.inserir_produto(p2)
carrinho.inserir_produto(p3)

carrinho.lista_produto()
print(carrinho.soma_total())