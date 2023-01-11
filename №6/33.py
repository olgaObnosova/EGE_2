for i in range(1000,-1,-1):
    s=i
    n=105
    while n>s:
        s+=3
        n=n-2
    if n==67:
        print(i)
    
