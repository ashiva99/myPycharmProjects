n=int(input("Enter size:"))
si=(n*2)-1
for i in range(si):
    for j in range(n):
        if i==0 or i==si-1:
            print("*"*(n-1),end="")
        else:
            print("~"*(n-1),end="")

        print("*")
