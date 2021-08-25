class Banco():
    def __init__(self):
        self.__agencias = [1111, 2222, 3333]
        self.__clientes = []
        self.__contas = []


    def inserir_cliente(self, cliente):
        self.__clientes.append(cliente)


    def inserir_conta(self, conta):
        self.__contas.append(conta)


    def autenticar(self, cliente):
        if cliente not in self.__clientes:
            return False

        if cliente.conta not in self.__contas:
            return False

        if cliente.conta.agencia not in self.__agencias:
            return False

        return True

