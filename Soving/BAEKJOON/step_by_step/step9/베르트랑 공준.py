li = [True for t in range(123456*2+1)]
for i in range(2, int((123456*2)**0.5)+1):
    if li[i] == True:
        j = 2
        while i * j <= 123456*2:
            li[i * j] = False
            j += 1
li[0] = False
li[1] = False

while True:
    n = int(input())
    if n == 0:
        break

    cnt = 0
    for i in range(n+1, 2*n+1):
        if li[i]:
            cnt += 1
    print(cnt)