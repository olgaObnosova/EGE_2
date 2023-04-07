for a in range(100):
    f = 1
    for x in range(1, 1000):
        f *= (x & 39 == 0 or x & 11 != 0 or x & a != 0)
    if f:
        print(a)
