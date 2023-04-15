import sys
input = sys.stdin.readline
def positive(n):
    if n>=0:
        return n
    else: return -n

N, M = map(int ,input().split())

x_list = []
y_list = []
for _ in range(M):
    x, y = map(int, input().split())
    x_list.append(x)
    y_list.append(y)
x_list.sort()
y_list.sort()
a, b = x_list[M//2], y_list[M//2]
answer = 0
for i in range(M):
    answer += positive(a-x_list[i]) + positive(b-y_list[i])
print(answer)