import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for _ in range(T):
    # 팀 개수, 문제 개수, 우리팀 ID, 로그 엔트리 개수
    n, k, t, m = map(int, input().split())
    # 팀 ID, 문제번호, 획득 점수
    logs = [list(map(int, input().split())) for _ in range(m)]
    answer = dict()
    cnt = dict()
    last = dict()
    idx = 0
    for i, j, s in logs:
        idx += 1
        last[i] = idx
        temp = answer.get(i, [0]*(k+1))
        if temp[j] < s:
            temp[j] = s
        cnt[i] = cnt.get(i, 0) + 1
        answer[i] = temp
    answer2 = []
    for key, val in answer.items():
        answer2.append([sum(val), cnt[key], last[key], key])
    answer2.sort(key = lambda x : (-x[0], x[1], x[2]))
    for idx, a in enumerate(answer2):
        if a[3] == t:
            print(idx+1)
            break
