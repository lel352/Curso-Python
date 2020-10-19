# Exercicio 2
# A segunda proposta que eu faço é um programa que pergunte a hora ao usuário baseando se no horário descrito
# exibe a saudação apropriada a exemplo de 0 aos 11 Bom dia 12 às 17.
# Boa tarde de 18 23.

hora = input('Que hora São (0-23)? ')
if hora.isnumeric():
    hora = int(hora)
    if 0 <= hora <= 11:
        print('Bom dia !!! ')
    elif 12 <= hora <= 17:
        print('Bom Tarde !!! ')
    elif 18 <= hora <= 23:
        print('Boa Noite !!!')
    else:
        print('Hora informada é inválida !!!')
else:
    print('Digite uma hora válida !!! \n Digite um horário entre 0 e 23.')
