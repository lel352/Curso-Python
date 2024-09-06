# Criando datas com módulo datetime
# datetime(ano, mês, dia)
# datetime(ano, mês, dia, horas, minutos, segundos)
# datetime.strptime('DATA', 'FORMATO')
# datetime.now()
# https://pt.wikipedia.org/wiki/Era_Unix
# datetime.fromtimestamp(Unix Timestamp)
# https://docs.python.org/3/library/datetime.html
# Para timezones
# https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
# Instalando o pytz
# pip install pytz types-pytz
from datetime import datetime


data = datetime(2022, 4, 20)
print(data)
data = datetime(2022, 4, 20, 15, 41, 23)
print(data)


data_str_fmt = '%Y-%m-%d %H:%M:%S'
data_str_data = '2022-04-20 07:49:23'
data2 = datetime.strptime(data_str_data, data_str_fmt)
print(data2)

data_str_fmt3 = '%d/%m/%Y'
data_str_data3 = '20/04/2022'
data3 = datetime.strptime(data_str_data3, data_str_fmt3)
print(data3)
