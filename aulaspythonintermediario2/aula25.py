def executa(funcao, *args):
    return funcao(*args)


# def soma(x, y):
#     return x + y


# def cria_multiplicador(multiplicador):
#     def multiplica(numero):
#         return numero * multiplicador
#     return multiplica


# duplica = cria_multiplicador(2)
duplica = executa(
    lambda m: lambda n: n * m, # lambda parametro: o que deve ser feito para o return
    2 # valores do paramentro
)
print(duplica(2))

print(
    executa(
        lambda x, y: x + y, # lambda parametro: o que deve ser feito para o return
        2, 3 # valores do paramentro
    ),
)

print(
    executa(
        lambda *args: sum(args),# lambda parametro: o que deve ser feito para o return
        1, 2, 3, 4, 5, 6, 7 # valores do paramentro
    )
)