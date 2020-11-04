"""
Aula 31 -  Listas em Python
Fatiamento
append, insert, pop, del, clear, extend, +
min, max
range
"""
# lista suporta vários valores
lista = [1, 2, 3, 4, 'Teste', True]

lista2 = ['A', 'B', 'C', 'D', 'E']

lista3 = ['A', 'Bacana', 'C', 'D', 'E', 10.5]

print(lista2[1])
print(lista3[1])
print(lista3[-1])
print(lista3)

lista3[5] = 'Qualquer outra coisa.'
print(lista3)

print(lista3[0:3])
print(lista3[1:4])
print(lista3[:4])
print(lista3[2:])
print(lista3[::2])
print(lista3[::-1])

l1 = [1, 2, 3]
l2 = [4, 5, 6]

l12 = l1 + l2

print(l12)

l4 = [1, 2, 3]
l5 = [4, 5, 6]
print(l4)
print(l5)
l4.extend(l5)  # adicionando os valores de l5 em l4
print(l4)
l4.extend('a')
print(l4)

l2.append('b')  # insere um novo valor no final da lista
print(l2)

l2.insert(0, 'c')  # Inserido 'b' no indice 0, primeiro campo é o a posição onde deseja inserir.
print(l2)

l2.pop()  # Remove o ultimo elemento
print(l2)

l3 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(l3)
del(l3[3:5])  # excluido os valores 4 e 5
print(l3)
l3.insert(0, 'b')
print(l3)
del(l3[0])
print(l3)

print(max(l3))
print(min(l3))
l3.pop(1)  # deletando o elemento no indice 1
print(l3)


l5 = list(range(1, 10))  # criando uma lista usando range
print(l5)

l6 = list(range(1, 100, 8))  # criando uma lista usando range de multiplos de 8
print(l6)


for valor in l6:
    print(valor)

l7 = ['String', True, 10, -20.2]

for valor in l7:
    print(f'O tipo de {valor} é {type(valor)}')

secreto = 'perfume'
digitadas = []
chances = 3

while True:
    if chances <= 0:
        print('Você perdeu !!!')

    letra = input('Digite uma letra: ')

    if len(letra) > 1:
        print('Digite somente uma letra.')
        continue

    digitadas.append(letra)

    if letra in secreto:
        print(f'{letra} existe na palavra secreta !!!')
    else:
        print(f'{letra} não existe na palavra secreta !!!')
        digitadas.pop()
        chances -= 1
        print(f'Você tem {chances} chances.')
        continue

    secreto_temporario = ''
    for letra_secreta in secreto:
        if letra_secreta in digitadas:
            secreto_temporario += letra_secreta
        else:
            secreto_temporario += '*'

    if secreto_temporario == secreto:
        print(f'Parabéns você acertou, palavra era {secreto_temporario} !!!')
        break
    else:
        print(f'A palavra secreta ta assim {secreto_temporario}')


