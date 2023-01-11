with open ('27B_25013092.txt') as f: # отработал минут 3 минуты моноблок
    n,k = map(int, f.readline().split())# отработал минут 4 минуты комп
    sp=[]
    count=0
    for i in range(k):
        sp.append(int(f.readline()))
        
    if sum(sp[:k//2])==sum(sp[k//2+1:]) and 0 in sp:
        count+=1
        #print(sp)
    for x in f.readlines():
        sp=sp[1:]+[int(x)]

        if 0 in sp and sum(sp[:k//2])==sum(sp[k//2+1:]):
            count+=1
            #print(sp)
print(count)
               
    
    
