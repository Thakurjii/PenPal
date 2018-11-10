#! usr/bin/python3

import getpass
from .database import store

def new_account():
    mail_id=int(input(' Enter your Gmail id > '))
    password=getpass.getpass(' Password > ')
    cnfm_pass=getpass.getpass(' Confirm Password > ')
    if password == cnfm_pass:
        save_dfl=input(' Make it default account [Y/n] >').lower()
        if save_dfl == 'y':
            store(mail_id,password)
        else:
            print()
        #Take input
        # call send_mail()        
    else:
        exit_app=input(''' 
        Password didn't matched.
        Press Y to retry or n to exit.
        [Y/n] > ''').lower()
        if exit_app == 'y':
            new_account()
        else:
            print(' >>> Thanks For Using <<<')

def fast_mail_with_atth():
    pass

def fast_mail_without_atth():
    pass

def send_mail(a,b,c,d):
    pass
