# Exercicio 3
# Terceiro é o seguinte faço um programa que peça o primeiro nome do usuário se o nome tiver quatro letras
# ou menos escreva seu nome é curto se tiver entre cinco e seis letras escreva seu nome é normal maior
# que 6 escreva seu nome é muito grande

nome = input('Digite nome: ')
tamanho = len(nome)
if tamanho <= 4:
    print('Seu nome é muito curto !!!')
elif tamanho <= 6:
    print('Seu nome é normal !!!')
elif tamanho > 6:
    print(' Seu nome é muito Grande !!!')
else:
    print('Nome Informado é inválido !!!')
