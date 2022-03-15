#Create a file with size of 4GB
import random

fl=open("C:\\Users\\user\\Desktop\\4gb_file.txt",'a')
for i in range(0,1053000000):
    fl.write(str(random.randint(1,120))+"\n")
fl.close()