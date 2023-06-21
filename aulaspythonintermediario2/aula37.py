# Introdução às Generator functions em Python
# generator = (n for n in range(1000000))


def generator(n=0):
    yield 1  # pausar
    print('Continuando...')
    yield 2 # Pausar
    print('Mais uma vez..')
    yield 3 # Pausar
    print('vou terminar')
    return 'Acabou'

gen = generator(n=0)
print(next(gen))
print(next(gen))
print(next(gen))


print()

def generator2(n=0, maximum=10):
    while True:
        yield n # pausar
        n += 1

        if n >= maximum:
            return


gen2 = generator2(maximum=100)
for n in gen2:
    print(n)