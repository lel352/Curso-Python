from datetime import datetime
from locale import setlocale, LC_ALL
from calendar import mdays
from calendar import monthrange

setlocale(LC_ALL, '')  # Vai tentar pegar o local padrão do computor do Usuario.
# setlocale(LC_ALL, 'pt_BR.utf-8') Dessa forma específica qual a localização deseja.


dt = datetime.now()
# =Dia, d=Numero do dia, %B=nome do mês, Y=ano em 4 digitos
formatacao = dt.strftime('%A, %d de %B de %Y')
formatacao2 = dt.strftime('%d/%m/%Y %H:%M:%S')


print(formatacao)
print(formatacao2)
print('*'*25)

# pega o último dia do mês, mas não funciona com ano bissexto
mes_atual = int(dt.strftime('%m'))
print(mdays)
print(mes_atual)
print(mdays[mes_atual])

print('*'*25)

# Retorna uma tupla contendo o número do dia na semana (0-6)
# e último dia de fevereiro de 2020
print(monthrange(2020, 2))
# O 5 significa que é um sábado
# O 29 significa que este é o último dia do mês
