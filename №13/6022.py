s = 'ABC BCKD CE DF EDH FE GIF HIFG IADE KDF'
d = {x[0]: x[1:] for x in s.split()}
print(d)


def f(str, end):
    if str[-1] == end and len(str) > 1:
        return 1
    elif str[-1] in str[:-1]:
        return 0
    return sum([f(str + x, end) for x in d[str[-1]]])


print(f('E', 'E'))
