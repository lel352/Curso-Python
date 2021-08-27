# https://docs.python.org/2/library/datetime.html
from datetime import datetime, timedelta

# strptime(string ,formato da data) cri um objeto de data apartir de uma string
# .strftime(formato da data) formatar um dada
# .timestamp obter o timestamp de um data
# fromtimestamp(valor do timestamp)  criar uma data de um timestamp

#   ano, mes, dia, hora, minuto, segundo
data = datetime(2019, 4, 20, 10, 53, 20)
print(data)
print('1*'*25)
print(data.strftime('%d/%m/%Y %H:%M:%S'))
print('2*'*25)
data2 = datetime.strptime('20/04/2019', '%d/%m/%Y') # coloca em formato padrão EUA
print(data2)
print('3*'*25)
print(data2.timestamp())
print('4*'*25)
data3 = datetime.fromtimestamp(1555729200.0)  # convertando timestamp em data
print(data3)
print('5*'*25)
data4 = datetime.strptime('20/04/1987 20:00:00', '%d/%m/%Y %H:%M:%S')
data4 = data4 + timedelta(days=5, seconds=59)
print(data4.strftime('%d/%m/%Y %H:%M:%S'))
data4 = data4 + timedelta(seconds=2*60*60) # Horas
print(data4.strftime('%d/%m/%Y %H:%M:%S'))
data4 = data4 + timedelta(seconds=59*60) # minutos
print(data4.strftime('%d/%m/%Y %H:%M:%S'))
print('6*'*25)
data1 = datetime.strptime('20/04/1987 20:00:00', '%d/%m/%Y %H:%M:%S')
data2 = datetime.strptime('25/04/1987 22:33:00', '%d/%m/%Y %H:%M:%S')
dif = data2 - data1
print(dif)
print(dif.seconds) # da hora
print(dif.total_seconds()) # diferencia em segundos da data e hora
print(dif.days) # somente os dias
print(data1.time()) # vendo somente a hora da data
print(data2 > data1)
print('7*'*25)