# import smtplib
# import os.path as op
# from email.mime.base import MIMEBase
# from email.mime.application import MIMEApplication
# from email.mime.multipart import *
# from email.mime.text import *
# from email.utils import COMMASPACE, formatdate
# from email import encoders
# from os.path import basename

# msg = MIMEMultipart()
# atth=r'C:\Users\Gaurav\Desktop\EBooks\t.txt'
# msg['From'] = 'gauravthakur40128@gmail.com'
# msg['To'] = 'gauravthakur40127@gmail.com'
# msg['Subject'] = 'Just to check mail api'
# message = 'Yup,It works...'
# msg.attach(MIMEText(message))

# try:
#     with open(atth, "rb") as fil:
#         part = MIMEApplication(
#             fil.read(),
#             Name=basename(atth)
#         )
#         # After the atth is closed
#         part['Content-Disposition'] = 'attachment; filename="%s"' % basename(atth)
#         msg.attach(part)
# except Exception as e:
#     print(e)

# mailserver = smtplib.SMTP('smtp.gmail.com',587)
# # identify ourselves to smtp gmail client
# mailserver.ehlo()
# # secure our email with tls encryption
# mailserver.starttls()
# # re-identify ourselves as an encrypted connection
# mailserver.ehlo()
# mailserver.login('gauravthakur40128@gmail.com', *****)

# mailserver.sendmail('gauravthakur40128@gmail.com','gauravthakur40127@gmail.com',msg.as_string())

# mailserver.quit()