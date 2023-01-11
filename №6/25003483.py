#https://kompege.ru/variant?kim=25003483
for i in range(1000,1,-1):
    s=i
    n=1
    while s<47:
        s=s+4
        n=n*2
    if n==64:
        print(i)
    
print(2**16)
