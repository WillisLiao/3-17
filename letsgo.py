import os
new_old_list = ['原型式號牌', '新式號牌']
plate_list = ['2-4', '4-2', '2-3', '3-2', '3-3', '2-2',
              '3-4', '3-3', '2-3']
# create folders and 5 .txt files under each folder
k= 0
count = 0
address = os.getcwd()
for i in range(2):
    
    os.mkdir(new_old_list[i])
    print("folder {} has been created!!".format(new_old_list[i]))
   
for i in range(6):
    file = open(f"{address}\\{new_old_list[0]}\\{plate_list[i]}.txt", 'w')
    print(f'{plate_list[i]}.txt has been created!')

for i in range(3):
    file = open(f"{address}\\{new_old_list[1]}\\{plate_list[i+6]}.txt", 'w')
    print(f'{plate_list[i+6]}.txt has been created')


# writing data to each .txt file    
#    for i in range(5):
 #       fivetimes += 1
 #       
 #       file = open(f"{address}\\{foldName}\\{newDir}_{count+fivetimes :02d}.txt", 'w')
 #       for g in range(3316):
 #           if data_into_list[g].split()[0]==str(count + fivetimes):
 #               file.write(f"{data_into_list[g]}\n")
 #           else:
 #               continue
 #       file.close() 
 #   count+=5


#name = list(input('你的名子: '))
#print(name)
#for i in range(len(name)):
#    print(name[i])

#determining if your name is in the list, if yes, 多少筆劃
#done_list = []
#n=-1
#for i in range(len(name)):
#    n+= 1
#    while True:
#        i+=1
#        if name[n] in data_into_list[i]:
#            print("word is in the list!")
#            done_list.append(data_into_list[i].split())

            
 #           break
 #       else:
 #           pass


#for i in range(len(done_list)):

 #   print(f"{done_list[i][1]}有{done_list[i][0]}筆劃")







        

                
                
            
                


