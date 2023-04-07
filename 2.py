a = int(input())
k = 1
sp = [0]
while sum(sp) < a:
    k = sp[-1] + 1
    if k == a:
        break
    sp.append(k)
print(sp)
