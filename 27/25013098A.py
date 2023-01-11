from collections import Counter
def delit(n):
    d=2
    c= Counter()
    while n%2==0:
        c.update([d])
        n//=2
    d=3
    while d*d<=n:
        if n%d==0:
            c.update([d])
            n=n//d
        else:
            d+=1
    if n!=1:
        c.update([n])
    return c
prav=0
i=0
with open('25013098A.txt') as f:
    n,m =map(int,f.readline().split())
    minlen=float('inf')
    dell=delit(int(f.readline()))
    for x in f.readlines():
        i+=1
        while len(dell)>=m:
            minlen=min(minlen,i-prav+1)
            lev=delit(x)
            dell=dell-lev
        dell=dell+delit(int(x))
print(minlen)
        
    
