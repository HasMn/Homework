#Create a file with size of 4GB and fill it with random values between 0-120.
import random
big_file_apath=input()
with open(big_file_apath,'w') as big_file:
    for i in range(0,1050000000):
        big_file.write(str(random.randint(0,120))+"\n")

mini_files_path=input()
#Split big_file into smaller files. Sort the small files.
with open(big_file_apath) as big_file:
    final_count={}
    for i in range(0,120):
        final_count.update({i: 0})
    for j in range(0,21):
        mini_count={}
        list = []
        for i in range(0,50000000):
            list.append(int(big_file.readline().rstrip()))
        list.sort()
        with open(mini_files_path+str(j)+".txt",'w') as mini_file:
            for k in list:
                mini_file.write(str(k)+"\n")
        for i in range(0,120):
            if i not in list:
                mini_count.update({i:0})
            else:
                mini_count.update({i:list.count(i)})
        for i in range(0,120):
            final_count.update({i: final_count[i]+mini_count[i]})

#Sort the big_file.
with open(big_file_apath,'w') as big_file:
    for i in range(0,120):
        if final_count[i]==0:
            pass
        else:
            for j in range(0,final_count[i]):
                big_file.write(str(i)+ "\n")






