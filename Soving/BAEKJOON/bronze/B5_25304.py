import sys
X = int(input())
N = int(input())
check = 0
for _ in range(N):
    a, b = map(int, input().split())
    check += a*b
if check == X:
    print("Yes")
else:
    print("No")