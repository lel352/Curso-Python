"""
Exercício com Abstração, Herança, Encapsulamento e Polimorfismo
Criar um sistema bancário (extremamente simples) que tem clientes, contas e
um banco. A ideia é que o cliente tenha uma conta (poupança ou corrente) e que
possa sacar/depositar nessa conta. Contas corrente tem um limite extra. Banco
tem clientes e contas.

Dicas:
Criar classe Cliente que herda da classe Pessoa (Herança)
    Pessoa tem nome e idade (com getters)
    Cliente TEM conta (Agregação da classe ContaCorrente ou ContaPoupanca)
Criar classes ContaPoupanca e ContaCorrente que herdam de Conta
    ContaCorrente deve ter um limite extra
    Contas têm agência, número da conta e saldo
    Contas devem ter método para depósito
    Conta (super classe) deve ter o método sacar abstrato (Abstração e
    polimorfismo - as subclasses que implementam o método sacar)
Criar classe Banco para AGREGAR classes de clientes e de contas (Agregação)
Banco será responsável autenticar o cliente e as contas da seguinte maneira:
    Banco tem contas e clentes (Agregação)
    * Checar se a agência é daquele banco
    * Checar se o cliente é daquele banco
    * Checar se a conta é daquele banco
Só será possível sacar se passar na autenticação do banco (descrita acima)
"""

from aulapythonpoo.exercicio01.banco import Banco
from aulapythonpoo.exercicio01.cliente import Cliente
from aulapythonpoo.exercicio01.conta import ContaCorrente, ContaPoupanca



banco = Banco()

cliente1 = Cliente('Luiz', 30)
cliente2 = Cliente('Maria', 18)
cliente3 = Cliente('João', 50)

conta1 = ContaPoupanca(1111, 254136, 0)
conta2 = ContaCorrente(2222, 254137, 0)
conta3 = ContaPoupanca(1212, 254138, 0)

cliente1.inserir_conta(conta1)
cliente2.inserir_conta(conta2)
cliente3.inserir_conta(conta3)


if banco.autenticar(cliente1):
    cliente1.conta.depositar(40)
    cliente1.conta.sacar(20)
else:
    print('Cliente não autenticado !!')

print('*'*20)

if banco.autenticar(cliente2):
    cliente2.conta.depositar(40)
    cliente2.conta.sacar(20)
else:
    print('Cliente não autenticado !!')

print('*'*20)
banco.inserir_cliente(cliente1)
banco.inserir_conta(conta1)
if banco.autenticar(cliente1):
    cliente1.conta.depositar(40)
    cliente1.conta.sacar(20)
else:
    print('Cliente não autenticado !!')

print('*'*20)
banco.inserir_cliente(cliente2)
banco.inserir_conta(conta2)
if banco.autenticar(cliente2):
    cliente2.conta.depositar(10)
    cliente2.conta.sacar(60)
else:
    print('Cliente não autenticado !!')

