#  Iterando strings com while em Python
#   Índices
frase = 'O rato roeu a roupa do rei de roma'
tamanho_frase = len(frase)
contador = 0
nova_string = ''

letra = input('Qual letra deseja colocar Maiúscula: ')

while contador < tamanho_frase:
    print(contador, frase[contador])
    if frase[contador] == letra:
        nova_string += letra.upper()
    else:
        nova_string += frase[contador]
    print(nova_string)
    contador += 1


print(nova_string)
