class CarrinhoDeCompras: # pode existir sem produtos, mas precisa dos produtos
    def __init__(self):
        self.__produtos = []

    def inserir_produto(self, produto):
        self.__produtos.append(produto)

    def lista_produto(self):
        for produto in self.__produtos:
            print(produto.nome, produto.valor)

    def soma_total(self):
        total = 0
        for produto in self.__produtos:
            total += produto.valor
        return total

class Produto: # produtos não depende do carrinhosdecompras
    def __init__(self, nome, valor):
        self.__nome = nome
        self.__valor = valor

    @property
    def nome(self):
        return self.__nome

    @property
    def valor(self):
        return self.__valor
