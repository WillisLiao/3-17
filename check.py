import re
txt = input('data: ')

if re.match(r'^(?=.*[0-9]{5})', txt) and re.match(r'^(?=.*[A-Z]{1})', txt) :
    print('match')

else:
    print('not match')


