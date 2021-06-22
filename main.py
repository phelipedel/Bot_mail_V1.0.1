import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from lib.utilidade import cor


email = '' #email
senha = input(str('Validacao de senha: ')) #senha
enviarpara = ('', '') #emails
assunto = 'Teste de envio de email automatico ' #assunto
mensage_html = '''     
<html>
  <head></head>
  <body>
    <p>Olá!<br>
       Como você está?<br>
       Aqui vai um <a href="https://www.youtube.com/">link</a> que talvez você goste.
    </p>
  </body>
</html>
'''


# nova instancia de MIMEMultipart
msg = MIMEMultipart()
msg['From'] = email
msg['To'] = enviarpara
msg['Subject'] = assunto
msg.attach(MIMEText(message, 'html'))

"""
# adicionando arquivos dentro do email
filename = ''  # nome do arquivo
filepath = ''  # caminho do arquivo
attachment = open(filepath, 'rb')

# criando o MIMEBase, sponsável por fazer a conversão correta do arquivo (base64)
att = MIMEBase('aplication', 'octet-stream')
att.set_payload(attachment.read())
encoders.encode_base64(att)

# para adicionar o arquivo ao email
att.add_header('Content-Disposition', f'attachment; filename= {filename}')
attachment.close()
msg.attach(att)
"""


# conecao ao sever
print(f'{cor.amarelo}Criando objeto servidor...')
server = smtplib.SMTP('smtp.office365.com', port=587)  # host e porta do hotmail
print(f'{cor.amarelo}Preparando para o envio...')
server.starttls()
server.login(email, senha)
server.sendmail(msg['From'], msg['To'], msg.as_string())

server.quit()
print(f'{cor.azul}Email enviado com sucesso')




"""
--------------------------------------------------------------
GMAIL:
servidor SMTP: smtp.gmail.com;
porta de saída: 465, caso esteja usando SSL ou 587 se for TLS.
--------------------------------------------------------------
HOTMAIL:     OBS HOTMAIL VARIAVEL, APENAS PARA TESTE SAIDA BASE ATUAL 587 O MESMO DO OUTOLOOK
servidor SMTP: smtp.live.com;
porta de saída: 25 ou 465.
--------------------------------------------------------------
YAHOO
servidor SMTP: smtp.mail.yahoo.com;
porta de saída: 465.
--------------------------------------------------------------
OUTLOOK.COM
servidor SMTP: SMTP.office365.com;
porta de saída: 587.
--------------------------------------------------------------
"""