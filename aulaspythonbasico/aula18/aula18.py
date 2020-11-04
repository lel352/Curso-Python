#  While/Else - Repetição com acumuladores em Python
"""
While / Else - Aula 8
Contadores
Acumuladores
"""

contador = 50

while contador < 100:
    print(contador)
    contador += 1


contador = 1
acumulador = 1

while contador <= 10:
    print(contador, acumulador)
    acumulador += contador
    contador += 1
else:
    print('Chegando no Else ')  # Se sair antes do laço terminar ele não entra aqui

contador = 1
acumulador = 1

while contador <= 10:
    print(contador, acumulador)
    if contador > 5:
        break

    acumulador += contador
    contador += 1
else:
    print('Chegando no Else ')  # Se sair antes do laço terminar ele não entra aqui