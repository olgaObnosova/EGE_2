with open('st_22_1.txt') as f:
    sp=[]
    maxx=0
    f=f.readlines()
    f=[int(line.rstrip()) for line in f]
    sp.append(f[0])
    #print(sp)
    k=0
    f.remove(f[0])
    while len(f)!=0:
        for x in f:
            if sp[-1]+5<=x:
                sp.append(x)
                #print(sp,x)
                f.remove(x)
        if len(sp)>=maxx:
            #print(sp)
            maxx=len(sp)
        sp=[]
        k+=1
        sp.append(0)
    print(maxx, k)



