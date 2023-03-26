import sys
sys.stdin = open("input.txt", "r")
board = input()
answer = ''
cnt = 0
for b in board:
    if b == '.':
        if cnt%2:
            print(-1)
            break
        answer += 'AAAA'*(cnt//4)
        cnt %= 4
        answer += 'BB'*(cnt//2)
        cnt = 0
        answer += '.'
    else:
        cnt += 1
else:
    if cnt % 2:
        print(-1)
    else:
        answer += 'AAAA' * (cnt // 4)
        cnt %= 4
        answer += 'BB' * (cnt // 2)
        print(answer)