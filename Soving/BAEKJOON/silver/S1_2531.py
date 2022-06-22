import sys
sys.stdin = open('input.txt', 'r')

# 접시 수, 초밥 가짓 수, 연속해서 먹는 접시 수, 쿠폰번호
N, d, k, c = map(int,input().split())
sushi = [0]
option = []
curr = 0
for _ in range(N):
    s = int(input())
    if s not in sushi and s != c:
        curr += 1
    sushi.append(s)
    option.append(curr)
max_sushi = 0
for i in range(N):
    if i+k >= N:
        a = option[N-1] - option[i]
        a += option[(i+k)%N]
    else:
        a = option[i+k] - option[i]
    for t in range(i, i+k):
        b = sushi[t%N]
        if b==c:
            a -= 1
    max_sushi = max(max_sushi, a)
print(max_sushi)