def f(n):
    s=''
    while n>0:
        s+=str(n%6)
        n=n//6
    return s[::-1]
for i in range(1,100):
    print(f(i)[-1])
