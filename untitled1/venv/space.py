#This program will remove unwanted spaces.
name=input('Enter string:')
name1=''
for i in range(len(name)):
    if not(name[i]==' ' and name[i+1]==' '):

        name1=name1+name[i]

print(name1)