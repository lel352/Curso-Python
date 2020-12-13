def aumento(valor, percentual):
    return valor + (valor * (percentual/100))


novoValor = aumento(50, 10)
print(f'novo valor é {novoValor:.2f}')
novoValor = aumento(100, 10)
print(f'novo valor é {novoValor:.2f}')
novoValor = aumento(10, 10)
print(f'novo valor é {novoValor:.2f}')
novoValor = aumento(15, 100)
print(f'novo valor é {novoValor:.2f}')
