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
from pytz import timezone

data = datetime.now()
print(data)
print(data.timestamp())  # Isso está na base de dados
print(datetime.fromtimestamp(1698859077))


data = datetime.now(timezone('Asia/Tokyo'))
print(data)

data = datetime(2024, 9, 3, 7, 49, 23, tzinfo=timezone('Asia/Tokyo'))
print(data)
