# Empacotamento e desempacotamento de dicionários
a, b = 1, 2
a, b = b, a # inverter valores
print(a, b) 


pessoa = {
    'nome': 'Aline',
    'sobrenome': 'Souza',
}

a, b = pessoa
print(a, b) # Keys chaves que vai imprimir
a, b = pessoa.values()
print(a, b)
a, b = pessoa.items()
print(a, b) # tuplas (valores), (chaves)

(a1, a2), (b1, b2) = pessoa.items()
print(a1, a2) # (chave, valor)
print(b1, b2) # (chave, valor)
print()

dados_pessoa = {
    'idade': 16,
    'altura': 1.6,
}

pessoas_completa = {**pessoa, **dados_pessoa} # estrair o valore de um dicionario **
print(pessoas_completa)
print()


# args e kwargs
# args (já vimos)
# kwargs - keyword arguments (argumentos nomeados)


def mostro_argumentos_nomeados(*args, **kwargs):
    print('NÃO NOMEADOS:', args)

    for chave, valor in kwargs.items():
        print(chave, valor)

print()
mostro_argumentos_nomeados(1,2, nome='Joana', qlq=123) # não nomeados: 1, 2 / Nomeados:  nome, qlq
print()
mostro_argumentos_nomeados(**pessoas_completa)
print()
configuracoes = {
    'arg1': 1,
    'arg2': 2,
    'arg3': 3,
    'arg4': 4,
}
mostro_argumentos_nomeados(**configuracoes)