import fnmatch as f


def delit(n):
    s = set()
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            if i % 2 == 0:
                s.add(i)
            if n // i % 2 == 0:
                s.add(n // i)
    return s


num = 0
for i in range(65_000, 650_000):
    if f.fnmatch(str(i), '6*97*5?') and len(delit(i)) >= 4:
        num += 1
        print(i, sum(delit(i)))
        if num == 7:
            break
