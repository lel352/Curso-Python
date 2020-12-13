def funcao1(arg):
    return arg()


def funcao2():
    return 10


print(funcao1(funcao2))
