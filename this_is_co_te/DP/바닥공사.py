d = [0]*1000

d[0] = 1
d[1] = 3

N = int(input())

for i in range(2, N):
    d[i] = d[i-1] + d[i-2]*2

print(d[N-1])