N, M = map(int, input().split())
li1 = []
answer = []

for i in range(N):
    li1.append(list(map(str,input())))

for j in range(N-7):
    for k in range(M-7):
        idx1 = 0
        idx2 = 0
        for x in range(j, j+8):
            for y in range(k, k+8):
                if (x+y) % 2 ==0:
                    if li1[x][y] != 'W':
                        idx1 += 1
                    if li1[x][y] != 'B':
                        idx2 += 1
                else:
                    if li1[x][y] != 'W':
                        idx2 += 1
                    if li1[x][y] != 'B':
                        idx1 += 1
        answer.append(idx1)
        answer.append(idx2)
print(min(answer))
