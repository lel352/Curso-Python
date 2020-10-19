#  Documentação e funções built-in úteis
# python não converte um dado para outro tipo dinamicamente o programador tem que mandar ele fazer isso
num1 = input('Número 1: ')
num2 = input('Número 2: ')

#isnumeric isdigit isdecimal
# Verificando se só tem numeros e positivos
print(num1.isnumeric())

# não preocupado com negativo e ponto flutuante
if num1.isdigit() and num2.isdigit():
    num1 = int(num1)
    num2 = int(num2)
    print(num1 + num2)
else:
    print('Não só pode números !!!')

