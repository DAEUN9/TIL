N, K = map(int, input().split())

A_li = list(map(int, input().split()))
B_li = list(map(int, input().split()))

A_li.sort()
B_li.sort(reverse=True)

for k in range(K):
    if A_li[k] < B_li[k]:
        A_li[k], B_li[k] = B_li[k], A_li[k]
    else:
        break
print(sum(A_li))