"""
Considerando duas listas de inteiros ou floats (lista A e lista B)
Some os valores nas listas retornando uma nova lista com os valores somados:
Se uma lista for maior que a outra, a soma só vai considerar o tamanho da
menor.
Exemplo:
lista_a     = [1, 2, 3, 4, 5, 6, 7]
lista_b     = [1, 2, 3, 4]
"""
lista_a     = [1, 2, 3, 4, 5, 6, 7]
lista_b     = [1, 2, 3, 4]


def soma_lista(l1, l2):
     intervalo = min(len(l1), len(l2))
     lista_soma = []
     for i in range(intervalo):
          lista_soma.append(l1[i] + l2[i])
     return lista_soma

          
print(soma_lista(lista_a,lista_b))



def soma_lista2(l1, l2):
     intervalo = min(len(l1), len(l2))
     return [l1[i] + l2[i] for i in range(intervalo)]

print(soma_lista2(lista_a,lista_b))



def soma_lista3(l1, l2):
     return [x + y for x, y in zip(l1, l2)]

print(soma_lista3(lista_a,lista_b))

