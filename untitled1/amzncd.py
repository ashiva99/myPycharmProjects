#input aaaabccdeeefggg --> we need to show first non repeating char
# output b

war=input('Enter string:')
d={}
for i in war:
    d[i]=d.get(i,0)+1
for j in war:
    if d[j]==1:
        print(j)
        break
