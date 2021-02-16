# * aula14 - Count - Contadores infinitos
# count - Itertools

from itertools import count


contador = count()
print(next(contador))
print(next(contador))
print(next(contador))
print(next(contador))

contador = count()
for valor in contador:
    print(valor)
    if valor >= 10:
        break

print('-'*25)
contador = count(start=5, step=2) # inicia em 5 pula em 2
for valor in contador:
    print(valor)
    if valor >= 10:
        break

print('-'*25)
contador = count(start=5, step=0.1) # inicia em 5 pula em 0.1
for valor in contador:
    print(round(valor, 2))
    if valor >= 10:
        break


print('-'*25)
contador = count(start=10, step=-1) # inicia em 10 pula em -1 laço invertido
for valor in contador:
    print(round(valor, 2))
    if valor <= -10:
        break

print('-'*25)
contador = count()
lista = ['Luiz', 'João', 'Paulo']
lista = zip(contador, lista)
print(list(lista))
