from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

def send_email(gmail_user, recipient, gmail_password, subject, body):
    msg = MIMEMultipart()
    message = body
    msg['From'] = gmail_user
    msg['To'] = recipient
    msg['Subject'] = subject

    msg.attach(MIMEText(message, 'plain'))
    server = smtplib.SMTP('smtp.gmail.com', port=587)
    server.starttls()
    server.login(msg['From'], gmail_password)
    server.sendmail(msg['From'], msg['To'], msg.as_string())
    server.quit()
