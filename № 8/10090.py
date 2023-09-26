import itertools as t

k = 0
# s1=list(t.product('123', repeat=3))
s2 = list(t.permutations('0234567', r=5))
print(s2[0])
for x in s2:
    x = ''.join(x)
    if x[0] != '0':
        fl = 1
        for i in range(len(x) - 1):
            if int(x[i]) % 2 == int(x[i + 1]) % 2:
                fl = 0
        if fl:
            k += 1
print(k)
