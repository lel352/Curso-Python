# Problema dos parâmetros mutáveis em funções

def lista_cliente(clientes_interavel, lista=[]):
    lista.extend(clientes_interavel)
    return lista


# problema gerado com parametro mutavel # lista=[]
clientes1 = lista_cliente(['João', 'Maria', 'Eduardo'])
clientes2 = lista_cliente(['Carlos', 'zico', 'jonas'])
print(clientes1)  # ['João', 'Maria', 'Eduardo', 'Carlos', 'zico', 'jonas']
print(clientes2)  # ['João', 'Maria', 'Eduardo', 'Carlos', 'zico', 'jonas']


# colocando nome é deixa de ser imutável
def lista_cliente2(clientes_interavel, lista=None):
    if lista is None:
        lista = []
    lista.extend(clientes_interavel)
    return lista


clientes1 = lista_cliente2(['João', 'Maria', 'Eduardo'])
clientes2 = lista_cliente2(['Carlos', 'zico', 'jonas'])
print(clientes1)  # ['João', 'Maria', 'Eduardo', 'Carlos', 'zico', 'jonas']
print(clientes2)  # ['João', 'Maria', 'Eduardo', 'Carlos', 'zico', 'jonas']
