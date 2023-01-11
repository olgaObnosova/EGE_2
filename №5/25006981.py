s=set()
for i in range(10,1001):

    a=bin(i)[2:]
    a=a[1:]
    for x in a:
        if x=='0':
            a=a[1:]
        else:
            break
    if len(a)!=0:
        s.add(i-int(a,2))
    else:
        s.add(i-0)
print(len(s))       
        
