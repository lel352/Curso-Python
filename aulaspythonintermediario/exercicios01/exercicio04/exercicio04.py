from random import randint
def fizzbuzz(numero):
    if numero % 3 == 0 and numero % 5 == 0:
        return 'fizzbuzz'
    if numero % 3 == 0:
        return 'fizz'
    if numero % 5 == 0:
        return 'buzz'
    return numero


for i in range(100):
    print(f'{i} é {fizzbuzz(i)}')
