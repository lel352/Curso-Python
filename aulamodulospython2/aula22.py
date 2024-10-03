# csv.writer e csv.DictWriter para escrever em CSV
# csv.reader lê o CSV em formato de lista
# csv.DictReader lê o CSV em formato de dicionário
import csv
from pathlib import Path
CAMINHO_CSV = Path(__file__).parent / 'aula22.csv'
lista_clientes = [
    {'Nome': 'Peter Parker', 'Endereço': 'Av 1, 22'},
    {'Nome': 'John Constantine', 'Endereço': 'R. 2, "1"'},
    {'Nome': 'Mary Jane', 'Endereço': 'Av B, 3A'},
]
with open(CAMINHO_CSV, 'w') as arquivo:
    nome_colunas = lista_clientes[0].keys()
    escritor = csv.DictWriter(
        arquivo,
        fieldnames=nome_colunas
    )
    escritor.writeheader()
    for cliente in lista_clientes:
        print(cliente)
        escritor.writerow(cliente)


lista_clientes = [
    ['Peter Parker', 'Av 1, 22'],
    ['John Constantine', 'R. 2, "1"'],
    ['Mary Jane', 'Av B, 3A'],
]

CAMINHO_CSV2 = Path(__file__).parent / 'aula22a.csv'

with open(CAMINHO_CSV2, 'w') as arquivo:
    # nome_colunas = lista_clientes[0].keys()
    nome_colunas = ['Nome', 'Endereço']
    escritor = csv.writer(arquivo)
    escritor.writerow(nome_colunas)
    for cliente in lista_clientes:
        escritor.writerow(cliente)
