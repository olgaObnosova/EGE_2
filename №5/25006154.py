#https://kompege.ru/variant?kim=25006154
for i in range(100000,1,-1):
    
    n=i-i%8
    n=bin(n)[2:]
    #print(n)
    if n.count('1')%2==0:
        n=n+'00'
    else:
        n=n+'01'
    if int(n,2)<353:
        print(i)
        break
