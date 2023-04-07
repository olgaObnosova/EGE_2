import itertools as t

k = 0
sp = list(t.permutations('МИТРОФАН', r=6))
for x in sp:
    x = ''.join(x)
    x = x.replace('М', "*")
    x = x.replace('Т', "*")
    x = x.replace('Р', "*")
    x = x.replace('Ф', "*")
    x = x.replace('Н', "*")
    x = x.replace('И', "@")
    x = x.replace('О', "@")
    x = x.replace('А', "@")
    if x.count('*') > x.count('@') and '@@' not in x:
        k += 1
print(k)
