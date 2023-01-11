def lower_bound(A, key):
    left=-1
    right = len(A)
    while right > left+1:
        middle= (left + right)//2
        if A[middle] >= key:
            right=middle
        else:
            left=middle
    return right
    
n=int(input())
A=list(map(int, input().split()))
k=int(input())
B=list(map(int, input().split()))
for i in range(len(B)):
    lb=lower_bound(A, B[i])
    if lb < len(A) and A[lb]==B[i]:
        print(lb+1, end = ' ')
    else:
        print(0, end = ' ')
