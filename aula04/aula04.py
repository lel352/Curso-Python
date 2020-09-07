"""
Tipos de dados
- Str - String
  Texto dentro de aspas simples ou duplas

- Int - Integer - Inteiro
  Número inteiro positivo ou negativo, zero entra, números sem ponto

- float - Real/Ponto Flutuante
  Número negativo ou positivo com ponto flutuante para separa as casas decimais . ex: 1.5

- bool - Boolean - Boleanno/lógico
  Só tem dois valores: True e False, Verdadeiro e Falso
"""
# type retorna o tipo desse valor
print('teste', type('teste'), sep=' = ')
print(123, type(123), sep=' = ')
print(1.5, type(1.5), sep=' = ')
print(False, type(False), sep=' = ')
print(10 == 10, type(10 == 10), sep=' = ')

# Converter tipo - Type cast
print('teste', type('teste'), bool('teste'))
print('10', type('10'), int('10'), type(int('10')))
print(float('25.5'))

print(10 + 10)
print('10' + '10')
print('10 + 10')

#  Nome
print('Leandro', type('Leandro'))
#  Idade
print(30, type(30))
#  Altura
print(1.75, type(1.75))
# Maior que 18 anos
print(30 > 18, type(30 > 18))
