with open('25014273B.txt') as f:
    sp=[]
    maxlen=0
    n, h, d = map(int, f.readline().split())
    f=[int(x) for x in f.readlines()]
    s=f[0]
    k=1
    for i in range(len(f)-1):
        if f[i]<f[i+1]:
            s+=f[i+1]
            k+=1
            sp.append((s,k))
        else:
            s=f[i+1]
            k=1
p=0         
for x in sp:
   if x[0]%h==0 and x[1]%d==0:
       maxlen=max(maxlen,x[1])
print(h,d)
#print(sp)
print(maxlen)          
