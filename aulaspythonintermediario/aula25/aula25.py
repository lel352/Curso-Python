from aulaspythonintermediario.aula25.vendas import calc_preco
from aulaspythonintermediario.aula25.vendas.formata.preco import real 

preco = 49.90
preco_aumento = calc_preco.aumenta(preco, 15, True)
print(preco_aumento)

preco_reducao = calc_preco.reducao(preco, 15)
print(preco_reducao)

print(real(preco_reducao))
