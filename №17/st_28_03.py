with open('17_st_28_03.txt') as f:
    mine = float('inf')
    maxx = k = 0
    sp = []
    for line in f:
        sp.append(int(line))
        if line[-1] == line[-2]:
            mine = min(mine, int(line))
for i in range(len(sp) - 1):
    if (str(sp[i])[-1] == str(sp[i])[-2] or str(sp[i])[-2] == str(sp[i])[-1]) \
            and ((abs(sp[i]) % 7 == 0 and abs(sp[i + 1]) % 7 != 0) or (abs(sp[i + 1]) % 7 == 0 and abs(sp[i]) % 7 != 0)) \
            and sp[i] ** 2 + sp[i + 1] ** 2 <= mine:
        k += 1
        maxx = max(maxx, sp[i] ** 2 + sp[i + 1] ** 2)
print(k, maxx)
