N = int(input())
cnt = 0
while N >= 0:
    if N%5 == 0:
        cnt += N//5
        break
    N -= 3
    cnt += 1
if N < 0:
    print(-1)
else:
    print(cnt)
