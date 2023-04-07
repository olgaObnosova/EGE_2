with open('17_7596.txt') as f:
    sp = []
    minn5 = float('inf')
    for x in f:
        if int(x) % 10 == 5 and len(str(int(x))) == 3:
            minn5 = min(minn5, int(x))
        sp.append(int(x))
k = m = 0
print(minn5)
for i in range(len(sp) - 1):
    if ((len(str(sp[i])) == 3 and len(str(sp[i + 1])) != 3) or \
        (len(str(sp[i + 1])) == 3 and len(str(sp[i])) != 3)) \
            and (sp[i] + sp[i + 1]) % minn5 == 0:
        k += 1
        m = max(m, sp[i] ** 2 + sp[i + 1] ** 2)
print(k, m)
