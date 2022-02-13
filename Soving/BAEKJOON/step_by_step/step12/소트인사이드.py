li = list(map(int, input()))
for i in range(len(li)-1):
    for j in range(len(li)-1-i):
        if li[j] < li[j+1]:
            li[j], li[j+1] = li[j+1], li[j]
for l in li:
    print(l,end='')
