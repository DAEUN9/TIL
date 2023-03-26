import sys
sys.stdin = open("input.txt", "r")
n = int(input())
answer = 1e9
for i in range(n//5+1):
    a = n - i*5
    if a%2 == 0:
        answer = min(a//2+i, answer)
if answer == 1e9:
    print(-1)
else:
    print(answer)