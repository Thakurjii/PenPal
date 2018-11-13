#! /usr/bin/python3

from .create import new_account
from .create import fast_mail_with_atth as fmwa
from .create import fast_mail_without_atth as fmwoa

#Function to select operation
def select_op(choice):
    if choice == 1:
        new_account()
    if choice == 2:
        fmwa()
    if choice == 3:
        fmwoa()
