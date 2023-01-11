k1,k0=0,0
for i in range(1,10000):
    k1,k0=0,0
    a=i
    a=bin(a)[2:]
    #print(a)
    for j in range(1,len(a),2):
        if a[j]=='1':
            k1+=1
    for j in range(0,len(a),2):
        if a[j]=='0':
            k0+=1
    if abs(k1-k0)==5:
        print(i)
