import sys
sys.stdin = open('input.txt', 'r')

N, M = map(int,input().split())
group1 = list(input())
group2 = list(input())
T = int(input())
d = dict()
for i in range(N):
    d[group1[i]] = 1
for j in range(M):
    d[group2[j]] = 2
merged_group = group1[::-1]+group2

for t in range(T):
    for k in range(N+M-1):
        if d[merged_group[k]]== 1 and d[merged_group[k+1]]== 2:
            merged_group[k], merged_group[k+1] = merged_group[k+1], merged_group[k]
            if merged_group[k+1] == group1[0]:
                break

print(''.join(merged_group))