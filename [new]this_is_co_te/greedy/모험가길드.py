import sys
sys.stdin = open("input.txt", "r")

# 모험가의 수
N = int(input())
# 모험가리스트
li = list(map(int, input().split()))
li.sort()
total = 0
cnt = 0
while li:
    target = li[0]
    while target != cnt:
        cnt = li[:cnt+1][-1]
        if cnt >= len(li):
            target = 1000
            break
        target = li[cnt-1]
    if target > len(li):
        break
    total += 1
    for i in range(target):
        li.pop(0)
print(cnt)