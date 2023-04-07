def f(a, b):
    if b == 0:
        return a
    elif a >= b:
        return f(a - b, b)
    elif a < b:
        return f(b, a)


for i in range(100):
    print(f(i, 14), i)
# k=0
# for i in range(123456795, 1234567888, 2):
#     if i%7!=0:
#         k+=1
# print(k)
