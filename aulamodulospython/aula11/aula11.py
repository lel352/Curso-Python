from string import Template
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import smtplib
from aulamodulospython.aula11.dados_email import meu_email, minha_senha


with open('template.html', 'r') as html:
    template = Template(html.read()) # enviando um arquivo String
    data_atual = datetime.now().strftime('%d/%m/%Y')
    corpo_msg = template.substitute(nome='Peter Parker', data=data_atual)  # Da erro se quantidade de placeholder e  parâmetro for diferentes


msg = MIMEMultipart()
msg['from'] = 'Teste'
msg['to'] = meu_email
msg['subject'] = 'Atenção: este é um e-mail de teste.'

corpo = MIMEText(corpo_msg, 'html')
msg.attach(corpo)

with open('Daredevil_Vol_1_4.jpg.', 'rb') as img: # rb modo leitura de bytes
    img = MIMEImage(img.read())
    msg.attach(img)

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    try:
        smtp.ehlo()
        smtp.starttls()
        smtp.login(meu_email, minha_senha)
        smtp.send_message(msg)
        print('E-mail enviado com sucesso')
    except Exception as e:
        print('Email não enviado !! Erro:',e)