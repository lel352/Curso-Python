# Groupby - Agrupando valores

from itertools import groupby, tee

alunos = [
   {'nome': 'Luiz', 'Nota': 'A' },
   {'nome': 'Marcia', 'Nota': 'B' },
   {'nome': 'José', 'Nota': 'C' },
   {'nome': 'André', 'Nota': 'A' },
   {'nome': 'Eduardo', 'Nota': 'D' },
   {'nome': 'João', 'Nota': 'B' },
   {'nome': 'Marcos', 'Nota': 'A' },
   {'nome': 'Maria', 'Nota': 'D' },
   {'nome': 'Fabrício', 'Nota': 'A' },
   {'nome': 'Leticia', 'Nota': 'C' },
   {'nome': 'Ana', 'Nota': 'A' }
]

alunos.sort(key=lambda item: item['Nota'])
print(alunos)
for aluno in alunos:
    print(aluno)


aluno_agrupados = groupby(alunos, lambda item: item['Nota'])
for agrupamento, valores_agrupados in aluno_agrupados:
    va1, va2 = tee(valores_agrupados)  # copiando os interadores
    print(f'Agrupamento: {agrupamento}')
    quantidade = len(list(va1))
    print(f'{quantidade} alunos tiraram a nota {agrupamento}')
    for aluno in va2:
        print(f'\t{aluno}')
    print()

