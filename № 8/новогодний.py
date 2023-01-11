from itertools import *
nachalo = "+781738"
cnt = 0
for x in product('0123456789', repeat=6):
    new_nomber = nachalo + ''.join(x)
    if '34' in new_nomber:
        continue
    if '0' in new_nomber:
        for i in range(1, len(new_nomber) - 1):
            #print(new_nomber[i])
            if (((int(new_nomber[i]) % 2 == 0 ) and \
                (int(new_nomber[i+1]) % 2 != 0)))\
                or (((int(new_nomber[i]) % 2 != 0) \
                    and (int(new_nomber[i+1]) % 2 == 0))):
                print(new_nomber)
                break
