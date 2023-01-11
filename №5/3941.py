#3941
def f(n):
    s=''
    while n>0:
        s=s+str(n%2)
        n=n//2
    return s[::-1]
count=0
for i in range(2,10000):
    a=i
    a=f(a)
    #print(a,'начальное')
    perv2=a[:2]
    #print(perv2,'первые две')
    nomer0=a.rfind('0')
    if nomer0!=-1:
        a=a[:nomer0]+perv2+a[nomer0+1:]
        #print(a)
    #else:
        #a='0'
    a=a[::-1]
    a=int(a,2)
    if a==127:
        count+=1
        print(i)
print(count)
