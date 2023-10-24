k = 0
for i in range(10_000_000, 100_000_000):
    n = bin(i)[2:]
    ost3 = bin(i % 3)[2:]
    if len(ost3) == 1:
        ost3 = '0' + ost3
    n = n + ost3
    ost5 = bin(i % 5)[2:]
    if len(ost5) == 1:
        ost5 = '00' + ost5
    if len(ost5) == 2:
        ost5 = '0' + ost5
    n = n + ost5
    r = int(n, 2)
    # print(r)
    if 1_111_111_110 <= r <= 1_444_444_416:
        k += 1
print(k)
