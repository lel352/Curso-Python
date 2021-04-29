from aulapythonpoo.aula01.pessoa import Pessoa

# criando um objeto apartir de uma classe
pessoa1 = Pessoa('Luiz', 31)
pessoa2 = Pessoa('Leandro', 30)

print(pessoa1)
print(pessoa2)
print('-'*25)
# criando um atributo que pertence somente essa pessoa1
pessoa1.nomeA = 'Luiz Teste'
print(pessoa1.nomeA)
pessoa1.comer('Arroz')
pessoa1.comer('Arroz')
pessoa1.para_comer()
pessoa1.comer('Arroz')
pessoa1.falar('POO')
pessoa1.para_comer()
pessoa1.para_comer()
pessoa1.falar('POO')
pessoa1.falar('POO')
pessoa1.para_falar()
pessoa1.comer('Arroz')
pessoa1.falar('POO')
pessoa1.para_falar()
pessoa1.para_comer()
pessoa1.para_comer()
pessoa1.falar('POO')
pessoa1.falar('POO')
pessoa1.comer('Arroz')
pessoa1.para_falar()
pessoa1.comer('Arroz')
pessoa1.falar('POO')
pessoa1.para_falar()
pessoa1.para_comer()
print('-'*25)

pessoa1.comer('Pão')
pessoa2.falar('Casa')

print('-'*25)

print(pessoa1.ano_atual)
print(pessoa2.ano_atual)
print(Pessoa.ano_atual)

print(pessoa1.get_ano_nascimento())
print(pessoa2.get_ano_nascimento())