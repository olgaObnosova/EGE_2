k = 0
for i in range(1000000000):
    n = bin(i)[2:]
    kc = kn = 0
    a = i
    for i in range(3):
        for x in str(a):
            if int(x) % 2 == 0:
                kc += 1
            else:
                kn += 1
        if kc > kn:
            n = n + '1'
        elif kn > kc:
            n = n + '0'
        elif kc == kn:
            if i % 2 == 0:
                n = n + '0'
            else:
                n = n + '1'
        a = int(n, 2)
    n = int(n, 2)
    if 123455 <= n <= 987654321:
        k += 1

print(k)
