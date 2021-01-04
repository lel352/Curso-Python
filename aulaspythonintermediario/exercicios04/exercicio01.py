String = '0123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789'
def funcao(texto):
    n = 10
    lista = [texto[i: i+n] for i in range(0, len(texto), n)]
    return '.'.join(lista)


print(funcao(String))
