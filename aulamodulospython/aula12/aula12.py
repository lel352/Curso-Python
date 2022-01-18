from zipfile import ZipFile
import os


caminho = r'C:\Users\desen\Downloads\serie2'
with ZipFile('arquivo.zip', 'w') as zip:
    for file in os.listdir(caminho):  # Só os arquivos da pasta, não entra nas subpastas
        caminho_completo = os.path.join(caminho, file)
        zip.write(caminho_completo, file) # o arquivo que quero salvar o nome que desejar ficar no arquivo


with ZipFile('arquivo.zip', 'r') as zip:
    for arquivo in zip.namelist():
        print(arquivo)


with ZipFile('arquivo.zip', 'r') as zip:
    zip.extractall('descompactado')