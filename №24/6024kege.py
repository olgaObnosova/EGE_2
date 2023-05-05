with open('24_6029.txt') as f:
    f = f.readline()
k = 1
maxx = 0
for i in range(len(f) - 1):
    if f[i] + f[i + 1] == 'EF' or f[i] + f[i + 1] == 'FE':
        k += 1
        maxx = max(maxx, k)
    else:
        k = 1
print(maxx)
