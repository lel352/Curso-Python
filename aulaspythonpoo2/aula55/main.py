from classe_contas import ContaCorrente, ContaPoupanca
from classe_cliente import Cliente
from classe_banco import Banco

c1 = Cliente('Peter', 30)
cc1 = ContaCorrente(111, 222, 0, 0)
c1.conta = cc1
c2 = Cliente('Mary Jane', 18)
cp1 = ContaPoupanca(112, 223, 100)
c2.conta = cp1
banco = Banco('Banco 1')
banco.clientes.extend([c1, c2])
banco.contas.extend([cc1, cp1])
banco.agencias.extend([111, 222])

if banco.autenticar(c1, cc1):
    cc1.depositar(10)
    c1.conta.depositar(100)
    print(c1.conta)
