a = 79 * '6'
while '2222' in a or '666' in a:
    if '2222' in a:
        a = a.replace('2222', '6', 1)
    else:
        a = a.replace('666', '2', 1)
print(a)
