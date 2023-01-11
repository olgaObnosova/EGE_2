with open('st_22_1.txt') as f:
    sp=[]
    maxx=0
    maxd=0
    f=f.readlines()
    f=[int(line.rstrip()) for line in f]
    sp.append(f[0])
    k=0
    for i in range(0,len(f)-1):
        for j in range(i+1,len(f)):
            

            if sp[-1]+5<=f[j]:
                sp.append(f[j])        
        if len(sp)>=maxx:
            maxx=len(sp)
            if sp[0]>maxd:
                maxd=sp[0]
            k+=1
        sp=[]
        sp.append(f[i])
    print(maxx,maxd, k)
