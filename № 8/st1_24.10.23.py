import itertools as t

sp = list(t.product('АВЕСТ', repeat=5))
k = 0
for x in sp:
    k += 1
    x = ''.join(x)
    if x == 'СВЕТА':
        print(k)
