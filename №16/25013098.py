def f(n):
    if n>10000:
        return n-10000
    else:
        return f(n+1)+f(n+2)
print(f(12345)*(f(10)-f(12))/f(11)+f(10101))
