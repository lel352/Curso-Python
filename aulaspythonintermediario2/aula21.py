# Operadores úteis:
# união | união (union) - Une
# Operadores úteis:
# união | união (union) - Une
# intersecção & (intersection) - Itens presentes em ambos
# diferença - Itens presentes apenas no set da esquerda
# diferença simétrica ^ - Itens que não estão em ambos
s1 = {1, 2, 3}
s2 = {2, 3, 4}
s3 = s1 | s2 # unir
print(s3) 
s3 = s1 & s2 # intersecção presente em ambos
print(s3)
s3 = s2 - s1 # diferença - Itens presentes apenas no set da esquerda neste caso o S2
print(s3) # R: 4
s3 = s1 - s2 # diferença - Itens presentes apenas no set da esquerda neste caso o S1
print(s3) # R: 1
s3 = s1 ^ s2 # diferença simétrica ^ - Itens que não estão em ambos
print(s3)