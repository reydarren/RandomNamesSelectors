import random

file = open('names.txt', 'r')
names = file.readlines()
file.close()

x = random.sample(names,input( "please enter the number of names needed: " ))
x = " ".join(x)
x = x.split("\n")
x = " ".join(x)
print(x)
