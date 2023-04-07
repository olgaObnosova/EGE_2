for x in '0123456789abcdef':
    a = int(f'57a{x}9', 16)
    b = 5 * int(f'{x}') + 4
    c = a * b
    x = c
    s = 0
    while c > 0:
        s += a % 12
        c = c // 12
    if s == 40:
        print(x)
