import random
letters='abcdefghijklmnopqrstuvwxyz'
numbers='0123456789'
x=''
y=''
for i in range(3):
    x=x+random.choice(numbers)
    y=y+random.choice(numbers)
    i+=1
print(x+y)
print(x)
print(y)
