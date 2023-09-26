import fnmatch as f


def delit(n):
    s = set()
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            s.add(i)
            s.add(n // i)
    return sum(s)


for i in range(13705, 10 ** 8):
    if f.fnmatch(str(i), '137?5'):
        d = delit(i)
        if d % 2024 == 0:
            print(i, d)
