with open('24_dos.txt') as f:
    f = f.readline()
maxx = 0
f = f.replace("QR", '*')
f = f.replace("RQ", '*')
f = f.replace("SR", '*')
f = f.replace("RS", '*')
f = f.replace("RR", '*')
f = f.replace("QS", '*')
f = f.replace("SQ", '*')
f = f.replace("QQ", '*')
f = f.replace("SS", '*')
f = f.split("*")
for x in f:
    maxx = max(maxx, len(x))
print(maxx)
