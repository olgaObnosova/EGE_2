import itertools as t

s = list(t.product('ЕКМОПРТЬЮ', repeat=5))
k = 0
for x in s:
    k += 1
    x = ''.join(x)
    if x[0] != 'Ь' and x.count('К') == 2 and k % 2 != 0:
        print(k)
