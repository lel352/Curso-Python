import random
import string

# Gera um número inteiro entre A e B
inteiro = random.randint(10, 20) # de 10 a 20
print(inteiro)

# Gerar um número Aleatório  usand a função range()
inteiro2 = random.randrange(900, 1000, 10) # Número aleatório entre 900 e 1000(não inclui o mil) pulando de 10 em 10
print(inteiro2)


# Gera um número flutuante entre A e B
flutuante = random.uniform(10, 20)
print(flutuante)

# Gera um número flutuante entre 0 e 1
flutuante2 = random.random()
print(flutuante2)

lista = ['Luiz', 'Otávio', 'Maria', 'Rose', 'Jenny', 'Danilo', 'Marcos']
# Seleciona Aleatórimente valores de uma lista
sorteio = random.choice(lista)
print(sorteio)
sorteio2 = random.choices(lista, k=2) # pegou dois da lista, pode repetir valores
print(sorteio2)
sorteio3 = random.sample(lista, 2) # pegou dois da lista, sem repetir valores
print(sorteio3)

# embaralhando a  lista
random.shuffle(lista)
print(lista)

# gera senha aleatória
letra = string.ascii_letters # retorna letras maiísculas e minúsculas
digitos = string.digits # 0..9
caracteres = '!@#$%$*._-'
geral = letra + digitos + caracteres

senha = "".join(random.choices(geral, k=20))
print(senha)

