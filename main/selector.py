#! /usr/bin/python3

import getpass

from .create import fast_mail_with_atth as fmwa
from .create import fast_mail_without_atth as fmwoa
from .create import new_account
from .database import retrieve


#Function to select operation
def select_op(choice):
    if choice == 1:
        new_account()
    if choice == 2:
        credentials=retrieve()
        mail_id,password=credentials[0].rstrip(),credentials[1]
        fmwa(mail_id,password)
    if choice == 3:
        credentials=retrieve()
        mail_id,password=credentials[0].rstrip(),credentials[1]
        fmwoa(mail_id,password)
