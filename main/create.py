#! /usr/bin/python3

import getpass
import os.path as op
import smtplib
from email import encoders
from email.mime.application import MIMEApplication
from email.mime.base import MIMEBase
from email.mime.multipart import *
from email.mime.text import *
from email.utils import COMMASPACE, formatdate
from os.path import basename

from .database import retrieve, store


#To add new Gmail account
def new_account():
    mail_id=input(' Enter your Gmail id > ')
    password=getpass.getpass(' Password > ')
    cnfm_pass=getpass.getpass(' Confirm Password > ')
    if password == cnfm_pass:

        save_dfl=input(' Make it default account [Y/n] >').lower()
        if save_dfl == 'y':
            store(mail_id,password)
            mail_from_default_acc()
        else:
            mail_from_new_acc(mail_id,password)
    else:
        exit_app=input(''' 
Password didn't matched.
Press Y to retry or n to exit.
[Y/n] > ''').lower()
        if exit_app == 'y':
            new_account()
        else:
            print('\n>>> Thanks For Using <<<')

#Send mail with Attachments
def fast_mail_with_atth(mail_id,password):
    recv_mail=input(' Message[\'To\'] > ')
    subject=input(' Message[\'Subject\'] > ')
    message=input('Enter Message > ')
    atth=input('Paste Attachment\'s Path Here > ')
    send_mail(mail_id,password,recv_mail,subject,message,atth)

def mail_from_default_acc():
    credentials=retrieve()
    mail_id,password=credentials[0].rstrip(),credentials[1]

    attach_choice=input('''
    Do you want to send mail with Attachments        
    Enter [Y/n] > ''').lower()
    if attach_choice == 'y':
        fast_mail_with_atth(mail_id,password)
    else:
        if attach_choice == 'n':
            fast_mail_without_atth(mail_id,password)
        else:
            print('Invalid Choice :(')

def mail_from_new_acc(mail_id,password):
    
    attach_choice=input('''
    Do you want to send mail with Attachments        
    Enter [Y/n] > ''').lower()
    if attach_choice == 'y':
        fast_mail_with_atth(mail_id,password)
    else:
        if attach_choice == 'n':
            fast_mail_without_atth(mail_id,password)
        else:
            print('Invalid Choice :(')

#Send mail without Attachments
def fast_mail_without_atth(mail_id,password):
    recv_mail=input(' Message[\'To\'] > ')
    subject=input(' Message[\'Subject\'] > ')
    message=input('Enter Message > ')
    send_mail(mail_id,password,recv_mail,subject,message)

def send_mail(mail_id,password,recv_mail,subject,message,atth=''):
    msg = MIMEMultipart()
    msg['From'] = mail_id
    msg['To'] = recv_mail
    msg['Subject'] = subject
    msg.attach(MIMEText(message))

    confirm = input(' Press Y to confirm or n to exit [Y/n] >').lower()
    if confirm == 'y':
        try:
            with open(atth, "rb") as fil:
                part = MIMEApplication(
                    fil.read(),
                    Name=basename(atth)
                )
                # After the atth is closed
                part['Content-Disposition'] = 'attachment; filename="%s"' % basename(atth)
                msg.attach(part)

        except Exception as e:
            pass

        mailserver = smtplib.SMTP('smtp.gmail.com',587)
        # identify ourselves to smtp gmail client
        mailserver.ehlo()
        # secure our email with tls encryption
        mailserver.starttls()
        # re-identify ourselves as an encrypted connection
        mailserver.ehlo()
        mailserver.login(mail_id, password)

        mailserver.sendmail(mail_id,recv_mail,msg.as_string())

        mailserver.quit()
    else :
        print('\n>>> Thanks For Using <<<')
