import os

# opening the file in read mode
my_file = open("newCharList.txt", "r", encoding= 'utf-8')
  
# reading the file
data = my_file.read()
  

# replacing end of line('/n') with ' ' and
# splitting the text it further when '.' is seen.
data_into_list = data.replace(',\n' , ' ').split(':')
  
# printing the data
print(data_into_list)
my_file.close()




# create folders and 5 .txt files under each folder
newDir = 'char'
k= 0
count = 0
address = os.getcwd()
for i in range(6):
    foldName = "{}{:02d}-{:02d}".format(newDir, k+1, k+5)
    if os.path.exists(foldName):
        print("{} fold is existed!".format(foldName))
    else:
        os.mkdir(foldName)
        print("folder {} has been created!!".format(foldName))
    print('Done!')
    k+=5
    fivetimes = 0
    
# writing data to each .txt file    
    for i in range(5):
        fivetimes += 1
        
        file = open(f"{address}\\{foldName}\\{newDir}_{count+fivetimes :02d}.txt", 'w')
        for g in range(3316):
            if data_into_list[g].split()[0]==str(count + fivetimes):
                file.write(f"{data_into_list[g]}\n")
            else:
                continue
        file.close() 
    count+=5


name = list(input('你的名子: '))
print(name)
for i in range(len(name)):
    print(name[i])

#determining if your name is in the list, if yes, 多少筆劃
done_list = []
n=-1
for i in range(len(name)):
    n+= 1
    while True:
        i+=1
        if name[n] in data_into_list[i]:
            print("word is in the list!")
            done_list.append(data_into_list[i].split())

            
            break
        else:
            pass


for i in range(len(done_list)):

    print(f"{done_list[i][1]}有{done_list[i][0]}筆劃")







        

                
                
            
                


