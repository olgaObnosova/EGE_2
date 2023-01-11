def f(n):
    if n==1:
        return 1
    elif n>1:
        return (3*n+5)*f(n-1)
print(f(100)/f(9))
