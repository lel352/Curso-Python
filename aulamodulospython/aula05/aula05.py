import os
import shutil

caminho_original = r'C:\Users\desen\Downloads\Arruma'
caminho_novo = r'C:\Users\desen\Downloads\serie2'

try:
    os.mkdir(caminho_novo)
except FileExistsError as e:
    print(f'Pasta {caminho_novo} já existe.')

for root, directs, files in os.walk(caminho_original):
    for file in files:
       old_file_path = os.path.join(root, file)
       new_file_path = os.path.join(caminho_novo, file)
       if 'Alien' in file:
           shutil.move(old_file_path, new_file_path)  # movendo de um caminho para o outro , com esse comando posso renomear o arquivo.
           print(f'Arquivo {file} movido com sucesso ! ')

       if '.txt' in file:
           shutil.copy(old_file_path, new_file_path)  # copiando um arquivo , com esse comando posso renomear o arquivo.
           print(f'Arquivo {file} copiado com sucesso ! ')


for root, directs, files in os.walk(caminho_novo):
    for file in files:
       old_file_path = os.path.join(root, file)
       new_file_path = os.path.join(caminho_novo, file)
       if '.txt' in file:
           os.remove(new_file_path)  # movendo de
           print(f'Arquivo {file} foi exluido com sucesso ! ')
       if 'alien' in file:
           os.remove(new_file_path)  # movendo de
           print(f'Arquivo {file} foi exluido com sucesso ! ')