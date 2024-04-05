#in this we are going to print the series like
#abcde
#xyz
#1234
#Then the output should be like this
#Output= ['ax1','by2','cz3','d4','e']
s1=input("Enter input string 1:")
s2=input('Enter input string 2:')
s3=input('Enter input string 3:')
i=j=k=0

while (i<len(s1) or j<len(s2) or k<len(s3)):
    output=''
    if i<len(s1):
        output=output+s1[i]
        i+=1
    if j<len(s2):
        output=output+s2[j]
        j+=1
    if k<len(s3):
        output=output+s3[k]
        k+=1
    print(output)
