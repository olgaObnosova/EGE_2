import itertools as d

k = 0
sp = list(d.product('ГЕКЭ023', repeat=4))
for x in sp:
    x = ''.join(x)
    k += 1
    if (x[0] == '0' or x[0] == '2' or x[0] == '3') and ('00' not in x and '22' not in x \
                                                        and '33' not in x and 'ГГ' not in x and 'ЕЕ' not in x and 'ЭЭ' not in x):
        print(k)
        break
