import sys

# Generator expression, Iterables e Iterators em Python
# Generator sabe pausar, ele pega um valor por vez.
iterable = ['Eu', 'Tenho', '__iter__']
iterator = iter(iterable)  # tem __iter__ e __next__
lista = [n for n in range(100)] # salva todos os valores na memoria, permtite tu acessar qualquer indice,
generator = (n for n in range(100)) # não salva todos os valores na memoria ele entrega um por vez , não permite acessar o indice por não term um.

print(sys.getsizeof(lista)) # tamalho em bytes
print(sys.getsizeof(generator)) 

print(generator)

for n in generator:
     print(n)