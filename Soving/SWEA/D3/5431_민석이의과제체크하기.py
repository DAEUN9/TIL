import sys

sys.stdin = open('sample_input.txt', 'r')

T = int(input())

for t in range(1, T+1):
    N, K = map(int, input().split())
    li = list(map(int, input().split()))
    answer = []
    for n in range(1, N+1):
        if n in li:
            continue
        else:
            answer.append(n)
    a = len(answer)
    for i in range(a-1):
        for j in range(i+1, a):
            if answer[i]>answer[j]:
                answer[i], answer[j] = answer[j], answer[i]
    print(f'#{t}', *answer)