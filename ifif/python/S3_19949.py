import sys
sys.stdin = open("input.txt", "r")
li = list(map(int, input().split()))
answer = 0
def solution(idx, score, before, cnt):
    global answer
    if idx >= 10:
        if score >= 5:
            answer += 1
        return
    for i in range(1, 6):
        if before == i:
            if cnt >= 2:
                continue
            if li[idx] == i:
                solution(idx + 1, score + 1, before, cnt + 1)
            else:
                solution(idx + 1, score, before, cnt + 1)
        else:
            if li[idx] == i:
                solution(idx + 1, score + 1, i, 1)
            else:
                solution(idx + 1, score, i, 1)
solution(0, 0, 0, 0)
print(answer)