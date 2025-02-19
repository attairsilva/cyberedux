from smtplib import SMTP_SSL
from email.mime.text import MIMEText

servidor = 'smtp.hostinger.com'
porta = 465

usuario = 'temp20@cybersocial.org.br'
senha = '@Aula321'

rem = usuario

des = 'attaircba@gmail.com'
corpo_email = '''
Teste email html v4!!!
'''

with open('assinatura.html', 'r') as arquivo:
    corpo_email += arquivo.read()

msg = MIMEText(corpo_email, 'html')
msg['Subject'] = 'Aula 17-02-2025 v4'
msg['From'] = rem

print('-'*80)
print(msg)
print('-'*80)

con = SMTP_SSL(servidor, porta)
con.login(usuario, senha)
con.sendmail(rem, des, msg.as_string())