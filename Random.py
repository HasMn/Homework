#Create a file with size of 4GB and fill it with random values between 0-120.
import random
big_file_apath=input()
with open(big_file_apath,'w') as big_file:
    for i in range(0,1050000000):
        big_file.write(str(random.randint(0,120))+"\n")

#Split big_file into smaller parts. Sort the small parts.
with open(big_file_apath) as big_file:
    final_count=[0]*121
    for i in range(0,1050000000):
        temp=int(big_file.readline().rstrip())
        list[temp]+=1

#Sort the big_file.
with open(big_file_apath,'w') as big_file:
    for i in range(0,120):
        if final_count[i]==0:
            pass
        else:
            for j in range(0,final_count[i]):
                big_file.write(str(i)+ "\n")

