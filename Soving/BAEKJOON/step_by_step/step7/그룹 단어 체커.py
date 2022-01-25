N = int(input())

cnt = 0
for i in range(N):    
    p = set()
    S = input()
    n = len(S)
    if n == 1:
        cnt += 1
        continue
    for j in range(1,n):
        a = S[j-1]
        if a == S[j]:
            if j == n-1:
                cnt += 1
                break
        else:
            if S[j] in p:
                break
            elif j == n-1:
                cnt += 1
                break
            p.add(a)

print(cnt)