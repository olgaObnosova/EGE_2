with open('24_7624.txt') as f:
    f = f.readline()
zapr = 'XYZ'
k = 1
maxx = 0
for i in range(len(f)):
    if not (f[i] in zapr and f[i + 1] in zapr):
        k += 1
        maxx = max(maxx, k)
    else:
        k = 1
print(maxx)
