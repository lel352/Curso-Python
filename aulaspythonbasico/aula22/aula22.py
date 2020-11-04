# Aula 22 - FOR / ELSE em Python

variavel = ['Luiz', 'AJoao', 'Maria']
for valor in variavel:
    print(valor)
    continue
    #break
    print(valor)


for valor in variavel:
    if valor.lower().startswith('j'):
        print('Começa com J')
        break
else:
    print('Não começa com J')

