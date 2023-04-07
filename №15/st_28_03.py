for a in range(500):
    f = 1
    for x in range(1000):
        f *= ((x & 144 != 0 or x & 94 != 0) <= (x & 73 != 0 or x & a != 0))
    if f:
        print(a)
