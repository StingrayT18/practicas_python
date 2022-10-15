import smtplib

from email.mime.text import MIMEText
msg=MIMEText("Contenido de correo")

msg['subject'] = 'Asunto del correo'
msg['From'] = 'desdedonde@gmail.com'
msg['To'] = 'haciadonde@gmail.com'

mailServer = smtplib.smtp('smtp.gmail.com', 587)
mailServer.ehlo()
mailServer.starttls()
mailServer.ehlo()
mailServer.login('augusto.tige@gmail.com', "xxxxxxxxx")
mailServer.sendmail('augusto.tige@gmail.com', 'augusto.tige@gmail.com', msg_as_string())

mailServer.close()



