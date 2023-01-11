count=0
for i in range(10000000):
    s=i
    s=s//7
    n=1
    while s<255:
        s+=n
        n+=1
    if n==7:
        count+=1
print(count)
