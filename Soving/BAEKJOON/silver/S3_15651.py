
N, M = map(int ,input().split())

answer = []

def suyeol():
    if len(answer)==M:
        print(*answer)
        return
    for i in range(1, N+1):
        answer.append(i)
        suyeol()
        answer.pop()
suyeol()