string=input("Enter the string:")
for i in range(0,len(string)):
    for j in range(0,i+1):
        print(string[j],end='')
    print()
