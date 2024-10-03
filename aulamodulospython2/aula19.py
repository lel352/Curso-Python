from pathlib import Path
from shutil import rmtree

caminho_projeto = Path()  # retorna o objeto
print(caminho_projeto)
print(caminho_projeto.absolute())

caminho_arquivo = Path(__file__)
print(caminho_arquivo)
print(caminho_arquivo.parent)
print(caminho_arquivo.parent.parent)

ideias = caminho_arquivo.parent / 'ideias'
print(ideias)
print(ideias / 'arquivos.txtf')

print(Path.home())
print(Path.home() / 'Desktop')

arquivo = Path.home() / 'Desktop' / 'arquivo.txt'
arquivo.touch()  # cria
arquivo.unlink()  # apaga

arquivo.touch()
arquivo.write_text('Olá mundo.')
print(arquivo.read_text())


caminho_arquivo = Path.home() / 'Desktop' / 'arquivo.txt'
caminho_arquivo.write_text('')
with caminho_arquivo.open('a+') as file:
    file.write('Uma linha 1\n')
    file.write('Uma linha 2\n')

print(caminho_arquivo.read_text())

caminho_pasta = Path.home() / 'Desktop' / 'Python é legal'
caminho_pasta.mkdir(exist_ok=True)  # criar pasta
sub_pasta = caminho_pasta / 'subpasta'
sub_pasta.mkdir(exist_ok=True)  # criar pasta

outro_arquivo = sub_pasta / 'arquivo.txt'
outro_arquivo.touch()
outro_arquivo.write_text('Hey')

mais_arquivo = caminho_pasta / 'arquivo.txt'
mais_arquivo.touch()
mais_arquivo.write_text('Hey')


caminho_pasta.rmdir()  # apagar pata, mas não apaga as pastas dentro das pastas


files = caminho_pasta / 'files'
files.mkdir(exist_ok=True)

for i in range(10):
    file = files / f'file_{i}.txt'
    if file.exists():
        file.unlink()
    else:
        file.touch()

    with file.open('a+') as text_file:
        text_file.write('ola mundo')
        text_file.write(f'file_{i}.txt')

rmtree(caminho_pasta)  # apaga todas as subpasta e aquivbos de uma pasta


def rmtree2(root, remove_root=True):
    for file in root.glob('*'):
        if file.is_dir():
            rmtree2(file, False)
            file.rmdir()
        else:
            file.unlink()

    if remove_root:
        root.rmdir()


rmtree2(caminho_pasta)
