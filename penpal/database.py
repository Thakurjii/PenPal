#! /usr/bin/python3

import os, sys, getpass

#USER_CREDENTIALS_FILE
FILE_PATH = r'C:\\Users\\'+getpass.getuser()+'\\AppData\\Local\\.PenPal' if sys.platform.lower().find("win") > -1 else r"/home/"+getpass.getuser()+"/.PenPal"
FILE_NAME = os.path.join(FILE_PATH,'database.pnpl')
#DEFAULT_EXCEPTION_MESSAGE
MESSAGE = 'Something went wrong.Please try to add account again.'

#To store credentials file
def store(mail_id,password):
    if not os.path.exists(FILE_PATH):
        os.makedirs(FILE_PATH)
    try:
        with open(FILE_NAME,'w') as fn:
            fn.write(mail_id+'\n'+password)

    except Exception:
        print('Something went wrong.Please try to add account again.')

#To retrieve data from credentials file
def retrieve():
    try:
        with open(FILE_NAME,'r') as fn:
            return fn.readlines()
    except Exception as e:
        print(MESSAGE)
