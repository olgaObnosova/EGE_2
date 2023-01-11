sp=set()
for i in range(1000):
    n=bin(i)[2:]
    if i%2==0:
        n= '1' + n+ '10'
    else:
        n = '11' + n + '0'
    n=int(n,2)
    if 800<=n<=1500:
        sp.add(n)
print(len(sp))
    
