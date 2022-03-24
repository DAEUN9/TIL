N = int(input())
li = list(map(int, input().split()))

d = [0]*N

d[0] = li[0]
d[1] = max(li[0], li[1])

for i in range(2, N):
    d[i] = max(d[i-2] + li[i], d[i-1])

print(d[N-1])