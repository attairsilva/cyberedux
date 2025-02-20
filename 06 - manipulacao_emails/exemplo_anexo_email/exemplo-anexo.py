from smtplib import SMTP_SSL
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart

from os.path import basename

import json

# carrega as configurações do arquivo config.json
with open('config.json', 'r') as arq:
    config = json.load(arq)

servidor = config['servidor']
usuario = config['usuario']
senha = config['senha']

remetente = usuario
destinatario = 'attaircba@gmail.com'

assunto = "Teste Arquivo Anexo"
corpo_email = "Teste de Envio com Python + Anexo"

arquivos_anexos = ['anexo.jpg', 'anexo1.jpg']

msg = MIMEMultipart()
msg['From'] = remetente
msg['Subject'] = assunto

msg.attach(MIMEText(corpo_email))

for arquivo_anexo in arquivos_anexos:
    with open(arquivo_anexo, "rb") as arq:
        part = MIMEApplication(
            arq.read(),
            Name=basename(arquivo_anexo)
        )

    part['Content-Disposition'] = 'attachment; filename="%s"' % basename(arquivo_anexo)
    msg.attach(part)

con = SMTP_SSL(servidor[0], servidor[1])
con.login(usuario, senha)
con.sendmail(remetente, destinatario, msg.as_string())