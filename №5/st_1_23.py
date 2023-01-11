for i in range(11000):
    n=i
    m=n
    n=bin(n)[2:]
    ch='1'*len(n)
    ch=int(ch)
    n=int(n)
    rez=ch-n
    rez=str(rez)
    R=m-int(rez,2)
    if R==999:
        print(i)
