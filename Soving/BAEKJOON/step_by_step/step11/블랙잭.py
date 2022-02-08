N, M = map(int,input().split())
cards = list(map(int, input().split()))
answer = []

for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            a = cards[i]+cards[j]+cards[k]
            if a <= M:
                answer.append(cards[i]+cards[j]+cards[k])
print(max(answer))