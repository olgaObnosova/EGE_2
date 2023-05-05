with open('27_B (3).txt') as f:
    k = int(f.readline())
    n = int(f.readline())
    sp = [int(x) for x in f]
maxc = maxn = max26 = maxs = 0
for i in range(k, n):
    if sp[i - k] % 26 == 0:
        max26 = max(max26, sp[i - k])
    elif sp[i - k] % 2 != 0:
        maxn = max(maxn, sp[i - k])
    if sp[i] % 26 == 0:
        maxs = max(maxs, sp[i] + maxn)
    elif sp[i] % 2 != 0:
        maxs = max(maxs, sp[i] + max26)
print(maxs)
