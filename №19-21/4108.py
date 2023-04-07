def f(s, c, m):
    if 30 <= s <= 45:
        return c % 2 == m % 2
    elif s > 45:
        return c % 2 != m % 2
    elif c == m:
        return False
    h = [f(s + 1, c + 1, m), f(s * 2, c + 1, m)]
    return any(h) if (c + 1) % 2 == m % 2 else all(h)


for s in range(1, 30):
    for m in range(5):
        if f(s, 0, m):
            if m == 3:
                print(s, m)
            break
