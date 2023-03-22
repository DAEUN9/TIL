import sys
sys.stdin = open("input.txt", "r")

N, M = map(int, input().split())
cnt = 0

if N > 0:
    books = list(map(int, input().split()))
    weight = 0
    for book in books:
        weight += book
        if weight > M:
            weight = book
            cnt += 1
    print(cnt + 1)
else:
    print(cnt)