"""
Comma Separated Values - CSV (Valores separados por vírgula)
É um formato de dados muito usado em tabelas (Excel, Google Sheets), bases de
dados, clientes de e-mail, etc...
"""

import csv

with open('clientes.csv', 'r') as arquivo:
    # dados = csv.reader(arquivo) # Um interador
    # print(dados)
    # next(dados) # não aparecer a primeira linha que é os nomes dos campos
    # for dado in dados:
    # print(dado)

    # dados = csv.DictReader(arquivo)  # transformer o CSV em um dicionário
    # for dado in dados:
    #    print(dado)
    #    print(dado['Nome'], dado['Sobrenome'])

    # esse for acima só funciona dentr do with

    # pegando os dado para usar em qualquer lugar
    dados = [x for x in csv.DictReader(arquivo)]


with open('clientes2.csv', 'w') as arquivo:
    escreve = csv.writer(
        arquivo,
        delimiter=',',
        quotechar='"',
        quoting=csv.QUOTE_ALL # colocar aspas duplas em cada valores
    )

    chaves = dados[0].keys()
    chaves = list(chaves)
    escreve.writerow(
        [
            chaves[0],
            chaves[1],
            chaves[2],
            chaves[3]
        ]
    )

    for dado in dados:
        escreve.writerow(
            [
                dado['Nome'],
                dado['Sobrenome'],
                dado['E-mail'],
                dado['Telefone']
            ]
        )