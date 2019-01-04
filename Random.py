import random

file = open('names.txt', 'r')
names = file.readlines()
file.close()

x = random.sample(names,input( "please enter the number of names needed" ))
print(x) 
