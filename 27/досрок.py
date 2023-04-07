maxx = maxxs = 0
with open('27B_7603.txt') as f:
    n = int(f.readline())
    sp = []
    k = int(f.readline())
    for i in range(k):
        sp.append(int(f.readline()))
    for x in f:
        maxx = max(maxx, sp[0])
        maxxs = max(maxxs, maxx + int(x))
        for i in range(len(sp) - 1):
            sp[i] = sp[i + 1]
        sp[-1] = int(x)
print(maxxs)
