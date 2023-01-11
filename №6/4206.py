for i in range(23,24):
    x = i
    #print(x)
    while x < 100:
      if x % 2 < 1:
        x = x // 2
      else:
        x = 3*x + 1
    print(x,i)
