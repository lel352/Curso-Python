def funcao1(funcao, *args, **kwargs):
    return funcao(*args, **kwargs)


def funcao2(nome):
    return f'Oi {nome}'


def funcao3(nome, saudacao):
    return f'{saudacao} {nome}'


executando = funcao1(funcao2, 'Luiz')
print(executando)
executando = funcao1(funcao3, 'Luiz', saudacao='Bom dia')
print(executando)
