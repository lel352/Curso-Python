# Aula 12 - len - Quantidade de caracteres
# Em Python tudo é objeto e tem metodos atrelados a eles

usario = input('Digite seu usuário: ')
quantidade = len(usario)
print(usario, quantidade, type(quantidade))
if quantidade < 6:
    print('Erro: precisa digitar pelo menos 6 caracteres')
else:
    print('Sucesso !!!')

string1 = input('Digite alguma coisa: ')
string2 = input('Digite outra coisa: ')
print(f'Quatidade Total de carecteres digitados {len(string1)+len(string2)}')


# Em Python tudo é objeto e tem metodos atrelados a eles
# o len é um método de um objeto
quantidade2 = string1.__len__() # Chamando o Len como método do objeto
print(quantidade2)
quantidade3 = len(string1)
print(quantidade3)
