sp=[0]*12346
for i in range(12345,0,-1):
    if i>10_000:
        sp[i]=i-10_000
    else:
        sp[i]=sp[i+1]+sp[i+2]
print(sp[12345]*(sp[10]-sp[12])/sp[11]+sp[10101])
