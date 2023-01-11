#4221
def f(n):
    s=''
    while n>0:
        s=s+str(n%4)
        n=n//4
    return s[::-1]
count=0
for i in range(1,10000):
    a=f(i)
    #print(a,'начальное')
    if i%2!=0:
        a='2'+a
        a=a+'11'
    else:
        a='13'+a
        a=a+'02'
    if int(a,4)>1000:
        print(int(a,4))
        break
    
   
