k = 0
s = 128 * '1'
while '333' in s or '11' in s:
    if '333' in s:
        s = s.replace('333', '1', 1)
    else:
        k += 2
        s = s.replace('11', '3', 1)
print(s)
print(k)
