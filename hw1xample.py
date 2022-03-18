import os.path
import re
while True:
    pw = input()
    if pw>6 and pw<20 and re.match(r'^(?=.*[a-zA-Z0-9_]{1})', pw) and re.match(r'^(?=.*[\W]{1})', pw) :

    

