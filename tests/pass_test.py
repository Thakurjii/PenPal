import getpass

pswd = getpass.getpass('Password:')

print(pswd)
p1='Gaurav'
#print(type(pswd))
if p1==pswd:
    print('Y')
else:
    print('N')