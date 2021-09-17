import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

##receiver = ''
##gmail_user = 
##gmail_password = 
###forming message using mime

body = '''

testing email functionality

'''

message = MIMEMultipart()
message['From'] = gmail_user
message['To'] = receiver
message['Subject'] = 'This email has an attacment, a pdf file'
message.attach(MIMEText(body, 'plain'))

##adding pdf to message
pdfname = 'KareemOtafyResume2021.pdf'

# open the file in bynary
binary_pdf = open(pdfname, 'rb')
payload = MIMEBase('application', 'octate-stream', Name=pdfname)
payload.set_payload((binary_pdf).read())

# enconding the binary into base64
encoders.encode_base64(payload)

# add header with pdf name
payload.add_header('Content-Decomposition', 'attachment', filename=pdfname)
message.attach(payload)
message = message.as_string()

#opening connection
server = smtplib.SMTP('smtp.gmail.com:587')
server.ehlo()
server.starttls()
server.login(gmail_user,gmail_password)

#mail loop
email = open("coemail.txt", "r")
for x in email:
  print(x[:-1])
  server.sendmail(gmail_user,x[:-1] , message)


server.quit()