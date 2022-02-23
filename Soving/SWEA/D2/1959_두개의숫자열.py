import sys

sys.stdin = open('input.txt', 'r')

T = int(input())

for t in range(1, T+1):
    N, M = map(int, input().split())
    A_li = list(map(int, input().split()))
    B_li = list(map(int, input().split()))

    # A리스트 길이가 더 작고 B리스트 길이가 더 크게끔
    if len(A_li) > len(B_li):
        A_li, B_li = B_li, A_li

    answer = []
    for b in range(len(B_li)-len(A_li)+1):
        total = 0
        for a in range(len(A_li)):
            total += B_li[b+a]*A_li[a]
        answer.append(total)

    max_total = answer[0]
    for an in answer:
        if max_total < an:
            max_total = an
    print(f'#{t}', max_total)
