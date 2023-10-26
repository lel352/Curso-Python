import copy

from aula50_package import produtos

# copy, sorted, produtos.sort
# Exercícios
# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)

def Imprimir(lista):
    print(*lista, sep='\n')


novos_produtos = [
    {**p, 'preco': round(p['preco'] * 1.1, 2) } 
    for p in produtos
    ]

Imprimir(produtos)    
print()
Imprimir(novos_produtos)

# Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)
produtos_ordenados_por_nome = copy.deepcopy(produtos)
produtos_ordenados_por_nome.sort(key=lambda item: item['nome'], reverse=True)
print()
Imprimir(produtos_ordenados_por_nome)
# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)
produtos_ordenados_por_preco = sorted(produtos, key=lambda item: item['preco'])
print()
Imprimir(produtos_ordenados_por_preco)
print()
Imprimir(produtos)    
