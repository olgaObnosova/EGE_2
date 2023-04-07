maxx = maxxs = 0
with open('27B_7603.txt') as f:
    n = int(f.readline())
    k = int(f.readline())
    sp = [int(x) for x in f]

for i in range(k, len(sp)):
    maxx = max(maxx, sp[i - k])
    maxxs = max(maxxs, maxx + sp[i])
print(maxxs)
