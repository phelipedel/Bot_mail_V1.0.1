import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from lib.utilidade import cor


email = '' #email
senha = input(str('Validacao de senha: ')) #senha
enviarpara = ('', '') #emails
assunto = 'Teste de envio de email automatico ' #assunto
mensagem = "Teste de mensagem "    #vericicar falha msg e no assunto 

#nova instancia de MIMEMultipart
msg = MIMEMultipart()
msg['Email'] = email
msg['Para'] = enviarpara
msg['Assunto'] = assunto

msg.attach(MIMEText(mensagem, 'plain'))

#conecao ao sever
server = smtplib.SMTP('smtp.office365.com', port= 587)  #host e porta do hotmail
#porta hotmaill variando possivel ecesso de envio automatico !?
server.starttls()
server.login(email,senha)
server.sendmail(msg['Email'], msg['Para'],mensagem)

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