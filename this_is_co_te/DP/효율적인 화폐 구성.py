# 화폐가치 N개, M원
N, M = map(int, input().split())
pay_li = [int(input()) for _ in range(N)]

d = [1001]*(M+1)
d[0] = 0
# 화폐 종류 돌기
for n in range(N):
    # 화폐로 만들 수 있는지 돌기
    for i in range(pay_li[n], M+1):
        # 저장된 값과 화폐로 새로만든 값중 작은값 고르기
        d[i] = min(d[i - pay_li[n]]+1, d[i])

if d[M]==1001:
    print(-1)
else:
    print(d[M])