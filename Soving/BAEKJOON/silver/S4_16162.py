import sys
sys.stdin = open("input.txt", "r")
N, A, D = map(int, input().split()) # 음 개수, 고음 첫 항, 공차
pitchs = list(map(int, input().split()))
try:
    start = pitchs.index(A)
    cnt = 1
    before = A
    for i in range(start+1, N):
        if before+D == pitchs[i]:
            cnt +=1
            before = pitchs[i]
    print(cnt)
except:
    print(0)