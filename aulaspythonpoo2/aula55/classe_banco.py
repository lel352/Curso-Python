import classe_contas
import classe_cliente


class Banco():
    def __init__(self, nome, agencias: list[int] | None = None, clientes: list[classe_cliente.Pessoa] | None = None, contas: list[classe_contas.Conta] | None = None):
        self._nome = nome
        self._agencias = agencias or []
        self._clientes = clientes or []
        self._contas = contas or []

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def agencias(self):
        return self._agencias

    @property
    def clientes(self):
        return self._clientes

    @property
    def contas(self):
        return self._contas

    def _checa_agencia(self, conta):
        if conta.agencia in self._agencias:
            return True
        return False

    def _checa_cliente(self, cliente):
        if cliente in self._clientes:
            return True
        return False

    def _checa_conta(self, conta):
        if conta in self._contas:
            return True
        return False

    def _checa_se_conta_e_do_cliente(self, cliente, conta):
        if conta is cliente.conta:
            return True
        return False

    def autenticar(self, cliente: classe_cliente.Pessoa, conta: classe_contas.Conta):
        return self._checa_agencia(conta) and self._checa_cliente(cliente) and self._checa_conta(conta) and self._checa_se_conta_e_do_cliente(cliente, conta)

    def add_cliente(self, cliente):
        self._clientes.append(cliente)

    def add_conta(self, conta):
        self._contas.append(conta)

    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'({self._agencias!r}, {self._clientes!r}, {self._contas!r})'
        return f'({class_name}{attrs})'
