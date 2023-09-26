def f(x):
    if x <= 2:
        return 2 ** x
    elif x > 2 and x % 2 == 0:
        return f(x // 2)
    elif x > 2 and x % 2 != 0:
        return f(x + 1) + f(x - 4)


print(f(4200))
