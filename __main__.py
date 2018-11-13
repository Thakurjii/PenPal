#! /usr/bin/python3

from main.selector import select_op

try:
    #Operations Choice
    choice=int(input('''
    1. Add new Gmail Account
    2. Fast Mail with Attachments
    3. Fast Mail without Attachments

    Choose [1 or 2 or 3] > '''))

    #Choice's Validation
    if choice not in [1,2,3]:
        print(' >>> Please select a valid  option. <<<')
    else:
        select_op(choice)

except Exception:
    print('Something went Wrong :(')