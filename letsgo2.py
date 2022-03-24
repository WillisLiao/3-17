import os
import re

from matplotlib.pyplot import get
new_old_list = ['原型式號牌', '新式號牌']
plate_list = ['2-4', '4-2', '2-3', '3-2', '3-3', '2-2',
              '3-4', '3-3', '2-3']

address = os.getcwd()
for i in range(2):
    if os.path.exists(new_old_list[i]):
        print("{} fold is existed!".format(new_old_list[i]))
    else:

        os.mkdir(new_old_list[i])
        print("folder {} has been created!!".format(new_old_list[i]))
   
for i in range(6):
    file = open(f"{address}\\{new_old_list[0]}\\{plate_list[i]}.txt", 'w')
    print(f'{plate_list[i]}.txt has been created!')

for i in range(3):
    file = open(f"{address}\\{new_old_list[1]}\\{plate_list[i+6]}.txt", 'w')
    print(f'{plate_list[i+6]}.txt has been created')
count = 0
while True:
    plate = input("plate: ")



       
    if re.fullmatch(r"[0-9]{2}-[A-Z]{2}", plate) or re.fullmatch(r"[A-Z]{2}-[0-9]{2}", plate):
        print('Yes')
        print(plate,'added')
        file = open(f"{address}\\原型式號牌\\2-2.txt", 'a+')
        file.write(f'\n{plate}')
        file.close()
    elif re.fullmatch(r"[0-9]{2}-[A-Z]{3}", plate) or re.fullmatch(r"[A-Z]{2}-[0-9]{3}", plate):
        print('Yes')
        print(plate,'added')
        file = open(f"{address}\\原型式號牌\\2-3.txt", 'a+')
        file.write(f'\n{plate}')
        file.close()
        file2 = open(f"{address}\\新式號牌\\2-3.txt", 'a+')
        file2.write(f'\n{plate}')
        file2.close()
    elif re.fullmatch(r"[0-9]{2}-[A-Z]{4}", plate) or re.fullmatch(r"[A-Z]{2}-[0-9]{4}", plate):
        print('Yes')
        print(plate,'added')
        file = open(f"{address}\\原型式號牌\\2-4.txt", 'a+') 
        file.write(f'\n{plate}')
        file.close()
    elif re.fullmatch(r"[0-9]{3}-[A-Z]{2}", plate) or re.fullmatch(r"[A-Z]{3}-[0-9]{2}", plate):
        print('Yes')
        print(plate,'added')
        file = open(f"{address}\\原型式號牌\\3-2.txt", 'a+')
        file.write(f'\n{plate}')
        file.close()
    elif re.fullmatch(r"[0-9]{3}-[A-Z]{3}", plate) or re.fullmatch(r"[A-Z]{3}-[0-9]{3}", plate):
        print('Yes')
        print(plate,'added')
        file = open(f"{address}\\原型式號牌\\3-3.txt", 'a+')
        file.write(f'\n{plate}')
        file.close()
        file2 = open(f"{address}\\新式號牌\\3-3.txt", 'a+')
        file2.write(f'\n{plate}')
        file2.close()
    elif re.fullmatch(r"[0-9]{4}-[A-Z]{2}", plate) or re.fullmatch(r"[A-Z]{4}-[0-9]{2}", plate):
        print('Yes')
        print(plate,'added')
        file = open(f"{address}\\原型式號牌\\4-2.txt", 'a+')
        file.write(f'\n{plate}')
        file.close()


#新式

    elif re.fullmatch(r"[0-9]{3}-[A-Z]{4}", plate) or re.fullmatch(r"[A-Z]{3}-[0-9]{4}", plate):
        print('Yes')
        print(plate,'added')
        file = open(f"{address}\\新式號牌\\3-4.txt", 'a+')
        file.write(f'\n{plate}')
        file.close() 
    elif plate =='--end-input--':
        break   
    else:
        print('no match')











        

                
                
            
                


