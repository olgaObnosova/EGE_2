import itertools as t

s = list(t.permutations('ЯРОСЛАВ', r=5))
k = 0
for x in s:
    x = ''.join(x)
    x = x.replace('Я', 'О')
    x = x.replace('А', 'О')
    x = x.replace('С', 'В')
    x = x.replace('Р', 'В')
    x = x.replace('Л', 'В')
    if x.count('В') > x.count('О') and 'ОО' not in x:
        k += 1
print(k)
