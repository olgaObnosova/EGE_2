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
    return c
print(delit(100000000))
