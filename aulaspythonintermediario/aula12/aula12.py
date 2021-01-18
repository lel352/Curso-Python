# Geradores, Iteradores e Iteráveis em Python

numero = 123
print(hasattr(numero, '__iter__')) # não é iterável
print('-'*23)
texto = 'String'
print(hasattr(texto, '__iter__'))  # é iterável

print('-'*23)
lista = [0, 1, 2, 3, 4, 5]  # é iterável
print(hasattr(lista, '__iter__'))
print(hasattr(lista, '__next__')) # não é um interador

# for transforma a lista em um iterador, para mostrar um de cada vez
for v in lista:
    print(v)

print('-'*23)

lista2 = iter(lista)
print(hasattr(lista2, '__next__')) #  agora lista dois é um interador
print('-'*23)
# interador da um valor de cada vez: abaixo mostra isso
print(next(lista2))  # 0
print(next(lista2))  # 1
print(next(lista2))  # 2
print(next(lista2))  # 3
print(next(lista2))  # 4
print('-'*23)
# Geradores;

import sys
import time

lista = list(range(10))
print(lista)
print('-'*23)
print(sys.getsizeof(lista))  # quanto de memória essa lista da gastando em byte
# gerador somente retorna o valor quando desejar assim não precisa ficar tudo na mesma lista oculpando memória

def gera():
    for n in range(100):
        yield n
        time.sleep(0.00001)

# to recebendo o valor um de cada vez.
g = gera()
print(hasattr(g, '__iter__'))
print(hasattr(g, '__next__')) # é um interador


for v in g:
    print(v)

print('-'*23)

def gera2():
    variavel = 'valor 1'
    yield variavel
    variavel = 'valor 1'
    yield variavel
    variavel = 'valor 1'
    yield variavel

g = gera2()
# cada vez que chamo a variável com next vou para o proximo valor
print(next(g))
print(next(g))
print(next(g))


# Criando com list Comprehension em Python

print('-'*23)
# lista salva todos os valores na memória
lista = [x for x in range(1000000)]  # com chaves vira lista
print(type(lista))
print(sys.getsizeof(lista))

# gerador não salva todos salva todos os valores na memória
lista2 = (x for x in range(1000000))  # com parêntese vira generator (gerador)
print(type(lista2))
print(sys.getsizeof(lista2))
# assim apresenta diferença de tamanho de memória


print('-'*23)
#  list, tuples, str -> Sequences -> interável

nome = 'Luiz Otávio'
# convete em tempo de execução em interador para usar o next, quando chega no final da erro pois não encontra mais termo
# assim o for sabe que terminou, faz tudo isso automaticamente
for letra in nome:
    print(letra)

print('-'*23)

interador = iter(nome)
# Usando esse comando posso agir como for usando o termo next
# chegando ao final do interador a variável é sempre limpada.
print(next(interador))
print(next(interador))
print(next(interador))
print(next(interador))
print(next(interador))
print(next(interador))
print(next(interador))
print(next(interador))
print(next(interador))
print(next(interador))
print(next(interador))

print(interador)
print('Como os valores do interador foram consumidos a variável não apresenta mais valor: \n Interador:')
for valor in interador:
    print(valor)


print('-'*23)
gerador = (letra for letra in nome)
print(next(gerador)) # L
print(next(gerador)) # U
print(next(gerador)) # i
print(next(gerador)) # z


# consumindo o restante do gerador
print('For gerador: ')
for valor in gerador:
    print(valor)

print('Como os valores do Gerador foram consumidos a variável não apresenta mais valor: \n Gerador:')
print(gerador)



print('Novo For gerador: ')
for valor in gerador:
    print(gerador)

    print('-' * 23)


