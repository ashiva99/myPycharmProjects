arr = []
for arrayy in range(20002):

    arr.append(0)

tree = []

for treee in range(60004):
    tree.append(0)

def build(node, lo, hi):
    if lo == hi:
        tree[node] = arr[lo]
    else:
        mid = (lo+hi)/2
        build(node*2, lo, mid)
        build(node*2+1, mid+1, hi)

        tree[node] = tree[node*2] & tree[node*2+1]

def query(node, lo, hi, i, j):
    if(lo>hi or lo >j or hi<i):
        return -1
    elif(lo>=i and hi <=j):
        return tree[node]
    else:
        mid = (lo + hi)/2

        q1 = query(node*2, lo, mid, i, j)
        q2 = query(node*2+1, mid+1, hi, i, j)

        return q1 & q2

tests = int(input())

def convertIntoInt(intNumbers):
    return [int(z) for z in intNumbers]

for aa in range(tests):
    intNumbers = input().split()
    intNumbers = convertIntoInt(intNumbers)
    n = intNumbers[0]
    k = intNumbers[1]

    for i in range(n):
        result = 0
        l = i-k
        r = i+k

        if(k>=n/2):
            result = query(1, 0, n-1, 0, n-1)
        elif l<0:
            result = query(1, 0, n-1, 0, r) & query(1, 0, n-1, n+1, n-1)
        elif r >= n:
            result = query(1, 0, n-1, l, n-1) & query(1, 0, n-1, 0, r-n)
        else:
            result = query(1, 0, n-1, l, r)

        print(result)


