import sys

N, K = map(int, sys.stdin.readline().split())
li = [int(sys.stdin.readline()) for n in range(N)]

end = max(li)
start = 1


while start<=end:
    answer = 0
    middle = (end + start) // 2
    for l in li:
        answer += l//middle
    if answer >= K:
        start = middle +1
    else:
        end = middle -1


print(end)