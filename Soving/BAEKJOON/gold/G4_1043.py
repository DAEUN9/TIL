import sys
sys.stdin = open('input.txt', 'r')

def find_set(n):
    temp = n
    while n!= people[n]:
        n = people[n]
    people[temp] = n
    return n

def union_set(x, y):
    x = find_set(x)
    y = find_set(y)
    people[y] = x


# 사람 수 N, 파티 수 M
N, M = map(int, input().split())
truth = list(map(int, input().split()))
people = [i for i in range(N+1)]
for i in range(1, truth[0]+1):
    people[truth[i]] = truth[1]

cnt = 0
resultpt = []
for m in range(M):
    party = list(map(int, input().split()))
    for i in range(1, party[0]):
       union_set(party[i], party[i+1])
    resultpt.append(party)
if truth[0]:
    for i in range(M):
        if find_set(truth[1]) != find_set(resultpt[i][1]):
            cnt += 1
else:
    cnt = M
print(cnt)



