N = int(input())
li = []
for n in range(N):
    a = int(input())
    li.append(a)

for i in range(N-1):
    for j in range(N-1-i):
        if li[j] > li[j+1]:
            li[j], li[j+1] = li[j+1], li[j]
for l in li:
    print(l)