#in this program we need to count the repeating strings
#input = aaabaccbdde
#output = 4a2b2c2d1e
s1=input("Enter the string")
d={}
output=''
for i in s1:
    d[i]=d.get(i,0)+1
for k,v in d.items():
    output=output+str(v)+k
print(output)

