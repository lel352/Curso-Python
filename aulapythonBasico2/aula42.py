""" while/else """
string = 'Valor qualquer'

i = 0
while i < len(string):
    letra = string[i]

    if letra == ' ':
        break # Else não será executado.

    print(letra)
    i += 1
else:
    print('Não encontrei um espaço na string.')
print('Fora do while.')