with open('25013098.txt') as f:
    maxc=0
    count=0
    f=f.readline()
    f=f.replace('AB','**')
    f=f.replace('CAC','***')
    for x in f:
        if x=='*':
            count+=1
        else:
            maxc=max(maxc,count)
            count=0
print(maxc)
