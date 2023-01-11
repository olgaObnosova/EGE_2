k=0
for x1 in '0123456789':
    for x2 in '0123456789':
        for x3 in '0123456789':
            for x4 in '0123456789':
                for x5 in '0123456789':
                    for x6 in '0123456789':
                        for x7 in '0123456789':
                            a=x1+x2+x3+x4+x5+x6+x7
                            f=int(a[6])**3
                            if a[0]!='0' and int(a[0])**2==int(a[1]+a[2]):
                                if len(str(f))==2:
                                    if a[4]+a[5] ==str(f):
                                        k+=1
                                elif len(str(f))==1:
                                    if a[5]==str(f):
                                        k+=1
                                else:
                                    if a[3]+a[4]+a[5] ==str(f):
                                        k+=1

print(k)
    
