import sys

N, K= map(int, sys.stdin.readline().split())

q = list(range(1, N+1))
print('<',end='')

i = K-1
while N>1:
    if i>=N:
        print(q.pop(i%N), end=', ')
        i %= N
    else:
        print(q.pop(i), end=', ')
    N -= 1
    i += K-1

print(str(q.pop())+'>')