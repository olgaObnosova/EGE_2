import fnmatch as f

# for i in range(1039485, 10**10):
#     if i%3013==0:
#         print(i)
#         break
for i in range(1039485, 10 ** 10, 3013):
    if f.fnmatch(str(i), '1?3948*5'):
        print(i)
