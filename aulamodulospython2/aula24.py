# secrets gera números aleatórios seguros
import secrets
import string as s
from secrets import SystemRandom as Sr

random = secrets.SystemRandom()
print('secrets.randbelow(100):', secrets.randbelow(100))
print('secrets.choice([10, 11, 12]): ', secrets.choice([10, 11, 12]))
# Funções:
# seed
#   -> NÃO FAZ NADA random.seed(10)
# random.randrange(início, fim, passo)
#   -> Gera um número inteiro aleatório dentro de um intervalo específico
r_range = random.randrange(10, 20, 2)
print('random.randrange(10, 20, 2): ', r_range)
# random.randint(início, fim)
#   -> Gera um número inteiro aleatório dentro de um intervalo "sem passo"
r_int = random.randint(10, 20)
print('random.randint(10, 20): ', r_int)
# random.uniform(início, fim)
#   -> Gera um número flutuante aleatório dentro de um intervalo "sem passo"
r_uniform = random.uniform(10, 20)
print('random.uniform(10, 20):', r_uniform)
# random.shuffle(SequenciaMutável) -> Embaralha a lista original
nomes = ['Peter', 'Mary', 'John', 'Natalia']
print(nomes)
# random.shuffle(nomes)
print(nomes)
# random.sample(Iterável, k=N)
#   -> Escolhe elementos do iterável e retorna outro iterável (não repete)
novos_nomes = random.sample(nomes, k=3)
print(nomes)
print('sample(nomes, k=3):', novos_nomes)
# random.choices(Iterável, k=N)
#   -> Escolhe elementos do iterável e retorna outro iterável (repete valores)
novos_nomes = random.choices(nomes, k=3)
print('random.choices(nomes, k=3): ', novos_nomes)
# random.choice(Iterável) -> Escolhe um elemento do iterável
print('choice(nomes):', random.choice(nomes))

print(s.ascii_letters, s.digits, s.punctuation)
print(''.join(Sr().choices(s.ascii_letters + s.digits + s.punctuation, k=64)))
print(''.join(Sr().choices(s.ascii_letters + s.punctuation + s.digits, k=12)))
# python -c "import string as s;from secrets import SystemRandom as Sr; print(''.join(Sr().choices(s.ascii_letters + s.punctuation + s.digits,k=12)))"
