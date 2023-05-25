with open('5134.txt') as f:
    n = int(f.readline())
    sp = []
    k = 0
    for line in f:
        sp.append(int(line))
# print(len(sp))
levind = 0
s = 1
for prind in range(len(sp)):
    s *= sp[prind]
    while s % 524288 == 0:
        s //= sp[levind]
        levind += 1
    k += abs(prind - levind + 1)
print(k)
