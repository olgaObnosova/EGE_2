for i in range(1000):
    s=i
    s=s//7
    n=1
    while s<255:
        if(s+n)%2==0:
            s=s+11
        n=n+5
    if n==106:
        print(i)
