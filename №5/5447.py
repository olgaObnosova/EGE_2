k=0
for i in range(1,1001):
    n=i
    for j in range(2):
        n=bin(n)[2:]
        if n.count('1')%2==0:
            n=n[1:]
        else:
            n=n.replace('0','')+'1'
        n=int(n,2)
    if n==7:
        k+=1
print(k)
