# https://docs.python.org/3/library/functions.html#open

import os

caminho_procura = input('Digite um Caminho: ') # r'C:\Users\desen\Downloads\Arruma' # input('Digite ')
termo_procura = input('Digite um termo para busca: ') # 'aranha' # input('Digite ')

def formata_tamanho(tamanho):
    base = 1024
    kilo = base
    mega = base ** 2
    giga = base ** 3
    tera = base ** 4
    peta = base ** 5

    if tamanho < kilo:
        texto = 'B'
    elif tamanho < mega:
        tamanho /= kilo
        texto = 'K'
    elif tamanho < giga:
        tamanho /= mega
        texto = 'M'
    elif tamanho < tera:
        tamanho /= giga
        texto = 'G'
    elif tamanho < peta:
        tamanho /= tera
        texto = 'T'
    else:
        tamanho /= peta
        texto = 'P'

    tamanho =  round(tamanho, 2)
    return f'{tamanho}{texto}'

conta =0
for root, direct, files in os.walk(caminho_procura):
    for file in files:
        if termo_procura.upper() in file.upper():
            try:
                conta += 1
                caminho_completo = os.path.join(root, file)
                nome_arquivo, extencao_arquivo = os.path.splitext(file)
                tamanho = os.path.getsize(caminho_completo) # tamanho em byte
                print()
                print('Encontrei o arquivo:', file)
                print('Caminho:', caminho_completo)
                print('Nome:', nome_arquivo)
                print('Extensão:', extencao_arquivo)
                print('Tamanho:', tamanho)
                print('Tamanho Formatado:', formata_tamanho(tamanho))

            except PermissionError as e:
                print('Sem Permissões.')
            except FileNotFoundError as e:
                print('Arquivo não encontrado.')
            except Exception as e:
                print('Erro desconhecido:',e)

print()
print(f'{conta} arquivos(s) encontrados(s).')

