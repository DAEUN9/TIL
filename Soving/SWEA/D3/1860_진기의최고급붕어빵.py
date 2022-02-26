import sys

sys.stdin = open('input.txt', 'r')

T = int(input())
for t in range(1, T+1):
    # 손님 수, 붕어빵 만드는 시간, 만드는 개수
    N, M, K = map(int, input().split())
    # 도착 초
    li = list(map(int, input().split()))

    check = [0]*(max(li)+1)
    answer = 'Possible'
    for l in li:
        check[l] += 1
    i = -1
    make = 0
    buy = 0
    for ch in check:
        i += 1
        if ch:
            buy += ch
        if i == M:
            make += K
            i = 0
        if buy > make:
            answer = 'Impossible'
            break
    print(f'#{t}', answer)
