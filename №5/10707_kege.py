def sh(n):
    s = ''
    while n > 0:
        s += str(n % 6)
        n = n // 6
    return s[::-1]


minn = 99999999999999999
for i in range(1, 1000):
    n = sh(i)
    if i % 3 == 0:
        n = n + n[:2]
    else:
        ost = sh(i % 3 * 10)
        n = n + ost
    r = int(n, 6)
    if r > 680:
        minn = min(minn, r)
print(minn)
