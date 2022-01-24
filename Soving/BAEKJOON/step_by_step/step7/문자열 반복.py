N = int(input())
li = []


for i in range(N):
    s = ''
    a, b = input().split()
    for j in b:
        s += j*int(a)
    print(s)