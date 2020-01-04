# coding: utf-8
import smtplib
import common.system_variable as s
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_text_mail(email, subject, text):
    server = smtplib.SMTP(s.MAILER_HOST, s.MAILER_PORT)
    server.starttls()
    server.login(s.MAILER_USERNAME, s.MAILER_PASSWORD)

    msg = MIMEMultipart()

    msg['From'] = s.MAILER_USERNAME
    msg['To'] = email
    msg['Subject'] = subject
    msg.attach(MIMEText(text, 'plain'))

    server.sendmail(s.MAILER_USERNAME, email, msg.as_string())
    server.quit()