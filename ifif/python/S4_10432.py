import sys
sys.stdin = open("input.txt", "r")
P = int(input())
N = 12
for p in range(1, P+1):
    answer = 0
    li = list(map(int, input().split()))[1:]
    for i in range(N-2):
        for j in range(i+2, N):
            a = li[i]
            b = li[j]
            c = max(a, b)
            for k in range(i+1, j):
                if li[k] > c:
                    continue
                break
            else:
                answer += 1
    print(p, answer)