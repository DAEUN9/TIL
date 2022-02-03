li = [True for t in range(10000+1)]
for i in range(2, int((10000)**0.5)+1):
    if li[i] == True:
        j = 2
        while i * j <= 10000:
            li[i * j] = False
            j += 1
li[0] = False
li[1] = False
sosu=[]
for i in range(10000+1):
    if li[i]:
        sosu.append(i)
T = int(input())
for i in range(T):
    n = int(input())
    a = n//2
    idx = 0
    while sosu[idx] < a:
        idx += 1
    while True:
        if (n - sosu[idx]) in sosu:
            b = n - sosu[idx]
            a = sosu[idx]
            break
        idx -= 1
    a, b = (a, b) if a <= b else (b, a)
    print(a, b)