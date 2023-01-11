def sumch(n):
    s=0
    while n>0:
        if n%10%2==0:
            s+=(n%10)
        n=n//10
    return s
def sumc(n):
    s=0
    for i in range(1,len(str(n)),2):
        s+=int(str(n)[i])
    return s
for i in range(100):
    if abs(sumch(i)-sumc(i))==9:
        print(i)

        
                   
