for i in range(100):
    a=bin(i)[2:]
    if i%2!=0:
        a='1'+a+'0'
    else:
        a='11'+a+'11'
    if int(a,2)<126:
        print(i,int(a,2))
        
    
