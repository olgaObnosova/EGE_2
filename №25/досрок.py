import fnmatch as f

for i in range(1200461, 10 ** 8):
    if i % 273 == 0:
        print(i)
        break
for i in range(1200654, 10 ** 8, 273):
    if f.fnmatch(str(i), '12??36*1'):
        print(i, i // 273)
