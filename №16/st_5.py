def f(n):
    if n > 1_000_000:
        return n
    return n + f(2 * n)


def g(n):
    return f(n) // n


zn = 2047
k = 0
for i in range(1, 1_000_000):
    if g(i) == g(1000):
        k += 1
print(k)
