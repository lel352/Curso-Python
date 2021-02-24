# Uso de try e except como condicional

def converte_numero(valor):
    try:
        valor = int(valor)
        return valor
    except ValueError:
        try:
            valor = float(valor)
            return valor
        except ValueError:
            pass


numero = converte_numero(input('Número: '))

if numero is not None:
    print(numero * 5)
else:
    print('Isso não é numero')
