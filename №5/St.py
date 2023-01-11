def chetn(x):
    s=0
    while x>0:
        if (x%10)%2==0:
            s+=x%10
        x=x//10
    return s
def cifr(x):
    summ=0
    for i in range(1,len(str(x)),2):
        summ+=int(str(x)[i])
    return summ
                   
                           
for i in range(1000):
    n=i
    
    
    m=abs(cifr(n)-chetn(n))
    #print(cifr(n))
    #print(chetn(n))
    #print(m)
    if m==13:
        print(i)
    
    
