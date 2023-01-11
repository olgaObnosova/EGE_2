for i in range(10,1000):
    sp=[]
    c=str(i)
    for j in range(len(c)-1):
        sp.append(int(c[j]+c[j+1]))
    maxx=max(sp)
    minn=min(sp)
    summ=maxx+minn
    if summ==137:
        print(sp)
        print(i)
