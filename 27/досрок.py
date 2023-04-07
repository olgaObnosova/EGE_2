import collections as d
maxx = maxxs = 0
with open('27B_7603.txt') as f:
    n = int(f.readline())
    sp = d.deque()
    k = int(f.readline())
    for i in range(k):
        sp.append(int(f.readline()))
    for x in f:
        maxx = max(maxx, sp[0])
        maxxs = max(maxxs, maxx + int(x))
        sp.popleft()
        sp.append(int(x))
print(maxxs)
