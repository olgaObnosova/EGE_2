k=0
for x in '012345678':
    for y in '012345678':
        for z in '012345678':
            for a in '012345678':
                for b in '012345678':
                    st = x+y+z+a+b
                    if st[0]!='0' and int(st[0])%2!=0 \
                       and st[-1]!='1' and st[-1]!='8':
                        k+=1
                    
print(k)    
