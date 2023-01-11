with open('25014273.txt') as f:
    f=[int(x) for x in f.readlines()]
maxs = k =0
for i in range(len(f)-1):
    for j in range(i+1,len(f)):
        if (f[i]+f[j])%120==0:
            maxs=max(maxs,f[i]+f[j])
            k+=1
print(k)
print(maxs)

