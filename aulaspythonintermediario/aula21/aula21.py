# Levantando exceções em Python (raise)

def divide(n1, n2):
    try:
        return n1 / n2
    except ZeroDivisionError as erro:
        print(erro)
        raise


print(divide(1, 2))
try:
    print(divide(1, 0))
except ZeroDivisionError as erro:
    print('erro: ', erro)


print('-'*25)
def divide2(n1, n2):
    if n2 == 0:
        raise ValueError("N2 não pode ser zero")
    return n1 / n2

try:
    print(divide2(1, 0))
except ValueError as erro:
    print('erro: ', erro)

try:
    print(divide2(1, 0))
except Exception as erro:
    print('erro: ', erro)


print('-'*25)
def divide3(n1, n2):
    try:
        return n1 / n2
    except ZeroDivisionError as erro:
        raise ValueError("N2 não pode ser zero")


try:
    print(divide3(1, 0))
except ValueError as erro:
    print('erro: ', erro)

try:
    print(divide3(1, 0))
except Exception as erro:
    print('erro: ', erro)