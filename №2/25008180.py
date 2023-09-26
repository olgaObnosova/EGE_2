print('x','y','w','z')
for x in 0, 1:
    for y in 0, 1:
        for w in range(2):
            for z in range(2):
                if ((w == z) or (x and (not y)) or w) == 0:
                    print(x, y, w, z)
