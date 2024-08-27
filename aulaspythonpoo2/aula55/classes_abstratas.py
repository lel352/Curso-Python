from abc import ABC, abstractmethod


class Conta(ABC):
    def __init__(self, agencia: int, numero_conta: int, saldo: float = 0):
        self._agencia = agencia
        self._numero_conta = numero_conta
        self._saldo = saldo

    @abstractmethod
    def sacar(Self, valor: float) -> float: ...

    @property
    def agencia(self):
        return self._agencia

    @property
    def numero_conta(self):
        return self._numero_conta

    @property
    def saldo(self):
        return self._saldo

    @agencia.setter
    def agencia(self, agencia: int):
        self._agencia = agencia

    @numero_conta.setter
    def numero_conta(self, numero_conta: int):
        self._numero_conta = numero_conta

    def depositar(self, valor: float) -> float:
        self._saldo += valor
        self.detalhes(f'(DEPÓSITO {valor:.2f})')
        return self.saldo

    def dados_completo_conta(self):
        return f'{self.agencia} / {self.numero_conta}'

    def detalhes(self, msg=''):
        print(F' O Seu saldo é {self.saldo:.2f} {msg}')

    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'({self.agencia!r}, {self.numero_conta!r}, {self.saldo!r})'
        return f'({class_name}{attrs})'
