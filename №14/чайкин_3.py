for x in range(1, 32):
    a = 7 * 32 ** 2 + 2 * 32 + x
    b = 32 ** 3 + 12 * 32 ** 2 + x * 32 + 7
    c = x ** 5
    if (a + b + c) % x == 0:
        print((a + b + c) // x, x)
