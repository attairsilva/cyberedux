from smtplib import SMTP_SSL
from email.mime.text import MIMEText

servidor = 'smtp.hostinger.com'
porta = 465

usuario = 'temp20@cybersocial.org.br'
senha = '@Aula321'

rem = usuario

des = 'angy15@e-record.com'
corpo_email = '''
Teste email html v3!!!
<br>
<p><strong><em><span style="color: #808080;">Fulano da Silva</span></em></strong></p>
<hr />
<p><span style="color: #808080;">CEO | MEI</span></p>
'''

msg = MIMEText(corpo_email, 'html')
msg['Subject'] = 'Aula 17-02-2025 v3'
msg['From'] = rem

print('-'*80)
print(msg)
print('-'*80)

con = SMTP_SSL(servidor, porta)
con.login(usuario, senha)
con.sendmail(rem, des, msg.as_string())