c = range(30, 46)
for a in range(1, 500):
    f = 1
    for x in range(1, 1000):
        f *= ((x % a == 0 and x in c) <= (x % 12 != 0))
    if f:
        print(a)
