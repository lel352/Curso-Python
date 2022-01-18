import subprocess

# windows - ping 127.0.0.1
# linux - ping 127.0.0.1 -c 4

proc = subprocess.run(
    ['ping', '127.0.0.1'],
    capture_output=True,  #  quer que a saída do comando vá uma variável, não em tela.
    text=True # saída formatada
)

print(proc)
print(proc.stderr)  # erro se tiver, caso não é None o retorno
print(proc.returncode)  # 0- se foi executado com sucesso
print(proc.args)  # Arqugmentos passados

print(proc.stdout)  # Saída do comando

saida = proc.stdout
saida = saida.replace('tempo', 'TEMPO DE RESPOSTA')
print(saida)