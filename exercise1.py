txt = input()
def fun1(txt):
    
    flag = 1
    if len(txt) ==12:
        for i in range(12):
            if i==4 or i==8:
                if txt[i] != '-':
                    flag = 0
                elif txt[i].isdecimal == False:
                    flag = 0
    else:
        flag = 0
    if flag==1:
        print('match')
        print(txt)
    else:
        print('not match')

fun1(txt)