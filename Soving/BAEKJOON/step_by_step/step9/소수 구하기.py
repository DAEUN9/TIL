M, N = map(int,input().split())
li = [True for t in range(N+1)]

for i in range(2, int(N**0.5)+1):
    if li[i] == True:
        j = 2
        while i * j <= N:
            li[i * j] = False
            j += 1
li[0] = False
li[1] = False

for i in range(M, N+1):
    if li[i]:
        print(i)