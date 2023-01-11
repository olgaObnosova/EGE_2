#https://kompege.ru/variant?kim=25006154
count=0
for i in range(10000):
    x=i
    s=5*(x//10)
    n=1
    while s<300:
        s=s+28
        n=n*3
    if n==243:
        count+=1
print(count)
