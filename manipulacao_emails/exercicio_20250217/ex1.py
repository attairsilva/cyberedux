from smtplib import SMTP_SSL

servidor = 'smtp.hostinger.com'
porta = 465

usuario = 'temp20@cybersocial.org.br'
senha = '@Aula321'

rem = usuario

des = 'angy15@e-record.com'
msg = 'Testando email pelo smtplib!!!'


con = SMTP_SSL(servidor, porta)
con.login(usuario, senha)
con.sendmail(rem, des, msg)