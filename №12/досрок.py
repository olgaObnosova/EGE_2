for i in range(3, 100):
    a = '3' + i * '5'
    s = 0
    while '25' in a or '355' in a or '555' in a:
        if '25' in a:
            a = a.replace('25', '3', 1)
        if '355' in a:
            a = a.replace('355', '52', 1)
        if '555' in a:
            a = a.replace('555', '23', 1)
    for x in a:
        s += int(x)
    if s == 27:
        print(i)
