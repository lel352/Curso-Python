from classes_abstratas import Conta


def validar_saque(saldo, valor_sacar, limite: float = 0):
    valor_pos_saque = saldo - valor_sacar
    if valor_pos_saque >= limite:
        return True
    return False


class ContaCorrente(Conta):
    def __init__(self, agencia: int, numero_conta: int, saldo: float = 0, limite: float = 0):
        super().__init__(agencia, numero_conta, saldo)
        self._limite_extra = limite

    @property
    def limite_extra(self):
        return self._limite_extra

    @limite_extra.setter
    def limite_extra(self, valor):
        self._limite_extra = valor

    def sacar(self, valor):
        limite_maximo = -self._limite_extra

        if validar_saque(self._saldo, valor, limite_maximo):
            self._saldo = self._saldo - valor
            return self._saldo

        print('Não foi possível sacar o valor desejado')
        print(f'Seu limite é {-self._limite_extra:.2f}')
        self.detalhes(f'(SAQUE NEGADO {valor:.2f})')
        return self._saldo

    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'({self.agencia!r}, {self.numero_conta!r}, {self.saldo!r}, {self.limite_extra!r})'
        return f'({class_name}{attrs})'


class ContaPoupanca(Conta):

    def sacar(self, valor):
        if validar_saque(self._saldo, valor, 0):
            self._saldo = self._saldo - valor
            self.detalhes(f'(SAQUE {valor:.2f})')
            return self.saldo

        print('Não foi possível sacar o valor desejado')
        self.detalhes(f'(SAQUE NEGADO {valor:.2f})')
        return self._saldo
