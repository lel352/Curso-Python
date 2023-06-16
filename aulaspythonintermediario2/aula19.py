# Sets - Conjuntos em Python (tipo set)
# Conjuntos são ensinados na matemática
# https://brasilescola.uol.com.br/matematica/conjunto.htm
# Representados graficamente pelo diagrama de Venn
# Sets em Python são mutáveis, porém aceitam apenas
# tipos imutáveis como valor interno.

# Criando um set
# set(iterável) ou {1, 2, 3}
# s1 = set('Leandro')
# s1 = set()  # vazio
# s1 = {'Leandro', 1, 2, 3}  # com dados

# Sets são eficientes para remover valores duplicados
# de iteráveis.
# - Seus valores serão sempre únicos;
# - Não aceitam valores mutáveis;
# - não tem índexes;
# - não garantem ordem;
# - são iteráveis (for, in, not in)
# Set não aceita valores mutáveis : s1 = {1,2,4,5,[3,3]} vai dar erro devido ao list 
s = {1, 2, 3, 3, 3, 3, 3, 1, (1345,2,)} # tupla é ele aceita.
print(s)

s1 = {1, 2, 3, 3, 3, 3, 3, 1}
print(s1)
l1 = [1, 2, 3, 3, 3, 3, 3, 1]
s1 = set(l1) 
l2 = list(s1)
print(l2)

print(3 not in s1)
print(4 not in s1)
print(3 in s1)
print(4 in s1)
for numero in s1:
     print(numero)

# Métodos úteis:
# add, update, clear, discard

# Operadores úteis:
# união | união (union) - Une
# intersecção & (intersection) - Itens presentes em ambos
# diferença - Itens presentes apenas no set da esquerda
# diferença simétrica ^ - Itens que não estão em ambos