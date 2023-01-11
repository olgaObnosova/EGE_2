#35
for i in range(1000,1,-1):
    print(i)
    
    s=i
    n=s
    s=s//10
    while s+n<125:
        s=s+n
        n=n-5
    if str(n)==2:
        print(i)
    print(n)
