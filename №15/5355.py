for a in range(1,100):
    f=1
    for x in range(1,1000):
        f*=(((x%2==0) <= (x%3!=0)) or (x+a>=80))
    if f:
        print(a)
        
