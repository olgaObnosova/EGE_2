#https://kompege.ru/variant?kim=25006891
for i in range(100,1000):
    a1=int(str(i)[0])**2+int(str(i)[1])**2
    a2=int(str(i)[1])**2+int(str(i)[2])**2
    s=str(max(a1,a2))+str(min(a1,a2))
    if int(s)==9010:
        print(i)
