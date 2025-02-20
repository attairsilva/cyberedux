from smtplib import SMTP_SSL
from email.mime.text import MIMEText
from dotenv import load_dotenv

import os

load_dotenv()

servidor = 'smtp.hostinger.com'
porta = 465

usuario = os.getenv('USUARIO')
senha = os.getenv('SENHA')

rem = usuario
des = 'attaircba@gmail.com'

msg = MIMEText('Testando email pelo smtplib v5!!!', 'plain')
msg['Subject'] = 'Aula 17-02-2025 v5-dotenv'
msg['From'] = rem

print('-'*80)
print(msg)
print('-'*80)

con = SMTP_SSL(servidor, porta)
con.login(usuario, senha)
con.sendmail(rem, des, msg.as_string())