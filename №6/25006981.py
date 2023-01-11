count=0
for i in range(1,10000):
    d=i
    n=8
    s=6
    while s<=1800:
        s=s+d
        n=n+7
    #print(n)
    if n==246:
        count+=1
print(count)
