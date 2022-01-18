from string import Template
from datetime import datetime

with open('template.html', 'r') as html:
    template = Template(html.read()) # enviando um arquivo String
    data_atual = datetime.now().strftime('%d/%m/%Y')
    corpo_msg = template.substitute(nome='Peter Parker', data=data_atual)  # Da erro se quantidade de placeholder e  parâmetro for diferentes
    #corpo_msg = template.safe_substitute(nome='Peter Parker', data=data_atual) # não da erro se quantidade de placeholder e parâmetro for diferentes

print(corpo_msg)