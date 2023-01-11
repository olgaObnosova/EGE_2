with open('st_15_12_22.txt') as f:
    maxx=0
    count=0
    f = f.readline().split('F')
    for x in f:
        if x.count('A')<=2:
            
            maxx=max(maxx,len(x))
print(maxx)
    
