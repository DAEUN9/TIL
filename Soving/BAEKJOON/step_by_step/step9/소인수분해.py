N = int(input())
a = 2
insu = []
while N > 1 :
    if N%a == 0:
        insu.append(a)
        N = N//a
        a = 2
    else:
        a += 1
for ins in insu:
    print(ins)