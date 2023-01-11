k=0
for x1 in 'АКЛОШ':
    for x2 in 'АКЛОШ':
        for x3 in 'АКЛОШ':
            for x4 in 'АКЛОШ':
                for x5 in 'АКЛОШ':
                    a=x1+x2+x3+x4+x5
                    #print(a)
                    k+=1
                    if a=='ШКОЛА':
                        print(k)
                        break
    
