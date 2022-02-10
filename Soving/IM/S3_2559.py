# 수열

N, K = map(int,input().split())
li = list(map(int, input().split()))
max_hap = sum(li[0:K])
hap = sum(li[0:K])
fir = li[0]
for n in range(1, N-K+1):
    hap = hap - fir + li[n+K-1]
    if max_hap < hap:
        max_hap = hap
    fir = li[n]
print(max_hap)