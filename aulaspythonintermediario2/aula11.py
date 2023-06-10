# Exercícios
# Crie funções que duplicam, triplicam e quadruplicam
# o número recebido como parâmetro.

# def duplicar(numero):
#    return numero * 2


# def triplicar(numero):
#    return numero * 3


#def quadruplicar(numero):
#    return numero * 4



def criar_multiplicar(multiplicador):
    def multiplicar(numero):
        return  numero * multiplicador
    return multiplicar

duplicar = criar_multiplicar(2)
triplicar = criar_multiplicar(3)
quadruplicar = criar_multiplicar(4)
nonuplicar = criar_multiplicar(9)


print(f'{duplicar(2)}')
print(f'{triplicar(2)}')
print(f'{quadruplicar(2)}')
print(f'{nonuplicar(2)}')