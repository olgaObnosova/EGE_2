import itertools as t

k = 0
sp = list(t.product('АВЛОР', repeat=4))
for x in sp:
    k += 1
    x = ''.join(x)
    if x[0] == 'Л':
        print(k)
        break
