import os
import hashlib
import re

address = os.getcwd()

class Error(Exception):
    pass

class ValueTooSmallError(Error):
    pass

class ValueTooLargeError(Error):
    pass
        
def setpw():
    while True:
        newpw = input('請輸入密碼: ')
        test_str = re.search("\W",newpw)

        try:
            if len(newpw)<6:
                raise ValueTooSmallError
            elif len(newpw)>20:
                raise ValueTooLargeError               
            elif re.match(r'^(?=.*[a-z]{1})', newpw) and re.match(r'^(?=.*[A-Z]{1})', newpw) and re.match(r'^(?=.*[0-9]{1})', newpw)and re.match(r'^(?=.*[\W]{1})', newpw) :
                pass                     
            break
        except ValueTooSmallError:
            print('密碼{}長度不夠長，請重新輸入密碼'.format(newpw))
            print()
        except  ValueTooLargeError:
            print('密碼{}長度太長，請重新輸入密碼'.format(newpw))    
            print()
        except test_str == None:
            print("密碼{}不包含特殊字元，請重新輸入密碼".format(newpw))
            print()
        except (re.search('\d', newpw)== None):
            print("密碼{}不包含數字，請重新輸入密碼".format(newpw)) 

               
    print('密碼設定完成 !')    
    print()   
    return newpw

count = 0
while True:
    if count >=1:
        inp = input('欲繼續輸入資料請按: 1 \n欲退出系統請按: 2\n')
        if inp =='2':
            break
    data = input('請輸入檔名: ')
    txt = "{}.txt".format(data)
    try:
        file = open(txt,"r")  
        print('該檔案已存在，請重新輸入檔名 !')
        print()
        count += 1
        continue

    except FileNotFoundError:
        f = open("{}\\{}.txt".format(address,data), 'w')    
        while True:    
            files = open(txt, 'a+', encoding= 'UTF-8')
            a = setpw()
            if a != '':
                files.write('{} \n'.format(setpw())) 
            else:
                print()
                count+=1
                break
print()
print('已結束系統')