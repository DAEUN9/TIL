import sys

sys.stdin = open('sample_input.txt', 'r')

T = int(input())

for t in range(1, T+1):
    N = int(input())
    O_mok = [input() for n in range(N)]

    answer = 'NO'
    # 오목 세로 판정
    for i in range(N):
        for j in range(N-4):
            k = 0
            while k < 5:
                if O_mok[i][j+k] == 'o':
                    k += 1
                else:
                    break
            if k == 5:
                answer = 'YES'
                break
        if k == 5:
            answer = 'YES'
            break

    # 오목 가로 판정
    for j in range(N):
        for i in range(N-4):
            k = 0
            while k < 5:
                if O_mok[i+k][j] == 'o':
                    k += 1
                else:
                    break
            if k == 5:
                answer = 'YES'
                break
        if k == 5:
            answer = 'YES'
            break

    # 오목 오른쪽 대각선 판정
    for i in range(N-4):
        for j in range(N-4):
            k = 0
            while k < 5:
                if O_mok[i+k][j+k]=='o':
                    k += 1
                else:
                    break
            if k == 5:
                answer = 'YES'
                break
        if k ==5:
            break

    # 오목 왼쪽 대각선 판정
    for i in range(N-4):
        for j in range(4, N):
            k = 0
            while k < 5:
                if O_mok[i+k][j-k] == 'o':
                    k += 1
                else:
                    break
            if k == 5:
                answer = 'YES'
                break
        if k == 5:
            break

    print(f'#{t}', answer)