# Try, Except - Tratando Exceções em Python
try:
    a = 1/0
    '''abc = {}
    print(abc[1])  # KeyError
    ab = []
    print(ab[1])  # IndexError
    print(a)  # NameErro'''
except NameError as erro:
    print('erro Name: ', erro)
except (IndexError, KeyError) as erro:
    print('erro de indice ou chave : ', erro)
except Exception as erro: # pega qualquer excessão
    print('erro Inesperado : ', erro)
else:
    print('Não teve erro')
finally:
    print('Vai sempre será executada. ')

