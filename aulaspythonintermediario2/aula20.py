
# Métodos úteis:
# add, update, clear, discard
s1 = set()
s1.add('Leandro')
s1.add(1)
s1.update(('Olá mundo', 1, 2, 3, 4))
print(s1)
s1.discard('Olá mundo') # eliminar o valor 
s1.discard('Leandro')
print(s1)
s1.clear()
print(s1)
# Operadores úteis:
# união | união (union) - Une