import sys
sys.stdin = open("input.txt", "r")
N = int(input())
answer = 0
levels = [int(input()) for _ in range(N)]
for i in range(N-2, -1, -1):
    if levels[i] >= levels[i+1]:
        answer += levels[i]-levels[i+1]+1
        levels[i] = levels[i+1]-1
print(answer)