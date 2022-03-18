import os.path
import re

class Error(Exception):
    pass

class PWTooSmallError(Error):
    pass

class PWTooLargeError(Error):
    pass

class FileAlreadyExists(Error):
    pass


address = os.getcwd()

while True:     
    name = input("filename: ")   
    if name != '--end-input--':
        try:              
            if  os.path.isfile(f"{name}.txt"):
                raise FileAlreadyExists             
            else:
                print("File not existed, creating file...\n")
                file = open(f"{address}\\{name}.txt", 'w')
                pass               
        except FileAlreadyExists:
            print("File already exists, please try again")
            continue
        while True:
     
                try:
                    file = open(f"{address}\\{name}.txt", 'a+') 
                    pw = input("password: ")
                    print()
                    if pw != '--end-input--':     
                            if len(pw)>20:
                                raise PWTooLargeError
                            elif len(pw)<6:
                                raise PWTooSmallError
                            else:
                                if re.match(r'^(?=.*[a-z]{1})', pw) and re.match(r'^(?=.*[A-Z]{1})', pw) and re.match(r'^(?=.*[0-9]{1})', pw)and re.match(r'^(?=.*[\W]{1})', pw) :

                                    file.write(f"{pw}\n")  
                                    file.close()
                                    print('Saved successfully!')
                                else:
                                    print("password must contain at least one of each: a-z, A-Z, 0-9, special_symbol")                   
                    else:
                        print()
                        break
                except PWTooSmallError:
                    print("password too small, please try again 6~20")
                except PWTooLargeError:
                    print("password too large, please try again 6~20")

    else:
        break
 