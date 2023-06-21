# Generator expression, Iterables e Iterators em Python
# Iterators entrega um valor por vez, classe com next
iterable = ['Eu', 'Tenho', '__iter__']
iterable = iter(iterable)  # tem __iter__ e __next__
print(next(iterable))
print(next(iterable))
print(next(iterable))


