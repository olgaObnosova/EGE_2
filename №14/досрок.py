for x in '0123456789abcde':
    a = int(f'97968{x}13', 15)
    b = int(f'7{x}213', 15)
    # print((a+b)%14)
    if (a + b) % 14 == 0:
        print(x, (a + b) // 14)
