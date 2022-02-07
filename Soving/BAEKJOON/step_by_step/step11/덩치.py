N = int(input())
li = []
for i in range(N):
    x, y = map(int,input().split())
    li.append((x,y))
answer = []
for j in range(N):
    rank = 1
    for k in range(N):
        if k == j:
            continue
        if li[j][0] < li[k][0]:
            if li[j][1] < li[k][1]:
                rank += 1
    answer.append(str(rank))

print(' '.join(answer))