import sys
sys.stdin=open("input.txt", "r")

N, M = map(int, input().split())
power_list = list(map(int, input().split()))
power_list.sort()
start, end = 0, N-1
answer = 0
while start < end:
    if power_list[start] + power_list[end] >= M:
        answer += 1
        start += 1
        end -= 1
    else:
        start += 1
print(answer)
