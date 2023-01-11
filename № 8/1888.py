k = 0
for x in 'KAPN':
    for x1 in 'KAPN':
        for x2 in 'KAPN':
            for x3 in 'KAPN':
                for x4 in 'KAPN':
                    for x5 in 'KAPN':
                        a = x+x1+x2+x3+x4+x5
                        if 'AA' not in a and 'KK' not in a and\
                             a.count('K')==2 and a.count('A')==2\
                               and a.count('P')==1 and a.count('N')==1:
                                k+=1
                            
print(k)
