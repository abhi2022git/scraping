import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import time
from datetime import date

def send(filename):
    from_user = "abhi2000thakurr@gmail.com"
    to_user = "avii2000thakurr@gmail.com"
    subject = "this is a subject"
    today = str(date.today()) + ".csv"

    msg = MIMEMultipart()
    msg['From'] = from_user
    msg['To'] = to_user
    msg['Subject'] = subject

    body = "this is a body part"
    msg.attach(MIMEText(body,'html'))


    my_file = open('stockdata.csv','rb')
    part = MIMEBase('application','octet-stream')
    part.set_payload(my_file.read())
    encoders.encode_base64(part)
    part.add_header('content-disposition','attachment; filename=' + today)
    msg.attach(part)
    message = msg.as_string()

    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login('abhi2000thakurr@gmail.com','cihpgpbajusiulnq')
    server.sendmail(from_user,to_user,message)
    server.quit()

