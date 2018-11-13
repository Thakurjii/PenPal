#! /usr/bin/python3

import os

#USER_CREDENTIALS_FILE
FILE_PATH=r'C:/Users/'+os.getlogin()+'/AppData/Local/.PenPal'
FILE_NAME=os.path.join(FILE_PATH,'database.pnpl')

#To store credentials file
def store(mail_id,password):
    if not os.path.exists(FILE_PATH):
        os.makedirs(FILE_PATH)
    try:
        with open(FILE_NAME,'w') as fn:
            fn.write(mail_id+'\n'+password)

    except Exception:
        print('Something went wrong.Please try to add account again.')