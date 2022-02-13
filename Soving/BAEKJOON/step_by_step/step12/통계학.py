import sys

N = int(input())
li = [int(sys.stdin.readline()) for i in range(N)]
li.sort()

an1 = round(sum(li)/N)
an2 = li[N//2]
an4 = li[-1] - li[0]
counter = [(li[0],1)]

cnt = 1
max_cnt = 1
for i in range(N-1):
    if cnt > max_cnt:
        max_cnt = cnt
    if li[i] == li[i+1]:
        cnt += 1
        counter.append((li[i+1], cnt))
    else:
        cnt = 1
        counter.append((li[i+1], cnt))

rank = 0
an3 = li[0]
for j in range(N):
    if counter[j][1] == max_cnt:
        rank += 1
        an3 = counter[j][0]
        if rank == 2:
            an3 = counter[j][0]
            break

print(an1)
print(an2)

print(an3)
print(an4)