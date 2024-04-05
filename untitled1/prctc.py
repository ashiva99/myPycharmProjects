
def invalid():
    print('invalid email id..')

mail = input('Enter email:')
att='@gmail.com'
j=0
if '@' in mail:
    for i in range(len(mail)):
        if mail[i]=='@':
            if mail[i:]==att:
                print('It is a valid email id..')
                break
            else:
                invalid()
                break
else:
    invalid()
