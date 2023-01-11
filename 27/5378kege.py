maxx = maxx2 = 0
with open('27.txt') as f:
    n, m = map(int, f.readline().split())
    sp = []
    for i in range(m * 2 + 1):
        a, b = map(int, f.readline().split())
        sp.append(a // 25 + bool(a % 25) + b // 25 + bool(b % 25))
        # print(sp)
    for x in f:
        if sum(sp) > maxx:
            maxx2 = maxx
            maxx = sum(sp)
        elif sum(sp)>maxx2:
            maxx2=sum(sp)
        for i in range(len(sp) - 1):
            sp[i] = sp[i + 1]
        a, b = map(int, x.split())
        sp[len(sp) - 1] = (a // 25 + bool(a % 25) + b // 25 + bool(b % 25))

print(maxx, maxx2)

# maxx=maxx2=0
'''
for i in range(len(sp)):
    if sum(sp[i:m*2+1])>maxx:
'''
