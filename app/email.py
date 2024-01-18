from threading import Thread
from flask import current_app
from flask_mail import Message
from app import mail
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send_email(subject, sender, recipients, text_body, html_body):
    smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
    smtpserver.ehlo()
    smtpserver.starttls()
    smtpserver.ehlo()
    smtpserver.login('twintech005@gmail.com', 'zlswsxdjfyviygqp')
    #smtpserver.sendmail(sender,recipients,text_body)
    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = recipients[0]
    #msg = Message(subject, sender=sender, recipients=recipients)
    part1 = MIMEText(text_body,'plain')
    part2=MIMEText(html_body,'html')
    msg.attach(part1)
    msg.attach(part2)
    smtpserver.sendmail(sender,recipients,msg.as_string())

#def send_email(subject, sender, recipients, text_body, html_body):
   # msg = Message(subject, sender=sender, recipients=recipients)
 #   msg.body = text_body
 #   msg.html = html_body
 #   Thread(
   #     target=send_async_email,
    #    args=(current_app._get_current_object(), msg)).start()
