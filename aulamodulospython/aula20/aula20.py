"""
Pilhas e filas
Pilha (stack) - LIFO - last in, first out. (último a entrar é o primeiro a sair)
    exemplo: pilha de livros que são adicionados um sobre o outro
Fila (queue) - FIFO - first in, first out. (primeiro a entar é o primero a sair)
    exemplo: Uma fila de banco (ou qualquer fila da vida real)
Filas podem ter efeitos colaterias em desempenho, porque a cada item alterado, todos os ìndices serão modificados.
"""
from collections import deque  # collections estruturas de dados de alto desempenho
from time import sleep

# Pilhas (stack)
livros = list()
livros.append('Livro 1')
livros.append('Livro 2')
livros.append('Livro 3')
livros.append('Livro 4')
livros.append('Livro 5')

print(livros)
livro_removido = livros.pop()  # removendo o último item da lista
print(livro_removido)
print(livros)

print('*'*25)

# Fila (queue)

fila = deque()
fila.append('pessoa 1')
fila.append('pessoa 2')
fila.append('pessoa 3')
fila.append('pessoa 4')
fila.append('pessoa 5')
fila.append('pessoa 6')
print(fila)

for nome in fila:
    print(nome)

print(f'Saiu: {fila.popleft()}')
print(f'Saiu: {fila.popleft()}')
print(f'Saiu: {fila.popleft()}')
print(f'Saiu: {fila.popleft()}')

print(fila)

print('*'*25)
fila2 = deque(maxlen=5) # máximo de elementos
fila2.extend([1, 2, 3, 4])
print(fila2)
fila2.append(5)
fila2.append(6)  # ele tirar o elemento mais antigo e coloca o novo elemento

print(fila2)

print('*'*25)
fila3 = deque(maxlen=10)  # mximo de elementos
for i in range(20):
    fila3.append(i)
    sleep(.1)
    print(fila3)


print('*'*25)
fila4 = deque(maxlen=10)  # mximo de elementos
fila4.extend([1, 2, 3, 4, 5, 6]) # adiciona na direita
fila4.insert(2, 'Luiz') # vai da erro se a fila estiver com valor máximo preenchida
print(fila4)
fila4.extendleft([0, -1])  # adiciona a esqueda
print(fila4)
print(fila4.index('Luiz'))  # pega a posição do valor 'Luiz'
print(fila4.index(3, 0, 6))  # pega a posição do valor 5, começando da posição 0 até a 5
fila4.reverse()
print(fila4)
fila4.rotate(2)  # pega os dois últimos elementos e coloca no começo da fila.
print(fila4)
