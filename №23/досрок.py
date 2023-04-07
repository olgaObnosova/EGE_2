def f(s, e):
    if s > e or s == 13:
        return 0
    elif s == e:
        return 1
    return f(s + 1, e) + f(s + 2, e) + f(s * 3, e)


print(f(3, 8) * f(8, 18))
