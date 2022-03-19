li = [0] * 30001

N = int(input())
for i in range(2, N+1):
    li[i] = li[i-1] + 1

    if li[i]%5 == 0:
        li[i] = min(li[i//5]+1, li[i])
    if li[i]%3 == 0:
        li[i] = min(li[i//3]+1, li[i])
    if li[i]%2 == 0:
        li[i] = min(li[i//3]+1, li[i])

print(li[N])