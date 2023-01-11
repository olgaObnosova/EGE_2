spD=[]
with open('24_25013092.txt') as f:
    sp=f.readline()
    count=kD=maxx=0
    for x in sp:
        spD.append(x)
        if spD.count('D')==3:
            maxx=max(maxx, len(spD)-1)
            spD=spD[spD.index('D')+1:]
print(maxx)
