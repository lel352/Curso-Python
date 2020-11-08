# Aula 27 - Expressão condicional com operador OR

nome = input('Nome: ')
if nome:
    print(nome)
else:
    print('Não digitou nada! ')

# Se nome for verdadeiro imprime nome senão imprime o que vem depois do or
print(nome or 'Você não digitou nada')

# caso chege na expressão verdadeiro ele para de verificar as outros
print(nome or None or False or 0 or 'Você não digitou nada')
print(nome or 'Você não digitou nada' or None or False or 0 or 'FIM')
print(nome or 'FIM' or None or False or 0 or 'TESTE')


# se nome for fazio/Verdadeiro teste recebe o valor dentro de nome ou o valor False se nome for vazio
teste = nome or False
print(teste)


idade = 10
# idade é meor que 19 é falso, assim ele vai para proxima expressão que nesse caso é o falso
maior = idade > 18 or False
print(maior)

a = 0 # 0 Retorna False
b = None # None Retorna False
c = False # None Retorna False
d = [] # Lista vazia Retorna False
e = {} # dicionario vazia Retorna False
f = 22 # Numero <> 0 Retorna True
g = 'Luiz' # String não vazia Retorna True

# o que achor verdadeiro primero vai para "variavel"
variavel = a or b or c or d or e or f or g
print(variavel)
variavel = a or b or c or d or e or g or f
print(variavel)

