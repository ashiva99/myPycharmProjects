#in this program we are counting the vowels
#input = shiva
#output = vowel a repeated 1 time
#          vowel i repeated 1 time
s1=input()
se={'a','e','i','o','u','A','E','I','O','U'}
d={}
for _ in s1:
    if _ in se:
        d[_]=d.get(_,0)+1

for k,v in sorted(d.items()):
    print(f'Vowel {k} repeated {v} times')