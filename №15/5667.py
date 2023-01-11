b=[]
for i in range(70,81):
    b.append(i)
for a in range(1,100):
    f=1
    for x in range(1,1000):
        f*=((x%a==0) or ((x in b) <= (x%18!=0)))
    if f:
        print(a)
