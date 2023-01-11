k=0
for i in range(4,11):
    s=''
    a=100
    while a>0:
        s+=str(a%i)
        a=a//i
    k+=i
    print(s[::-1], i)
print(k)
