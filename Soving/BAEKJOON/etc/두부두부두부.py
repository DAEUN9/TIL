from collections import deque

N, M, K = map(int, input().split())

dubu = deque([i for i in range(1, N+1)])

if K>3:
    a = 3-K
    dubu.rotate(a)
    print(dubu[M-1])
elif K<3:
    a = 3-K
    dubu.rotate(a)
    print(dubu[M-1])
else:
    print(M)


# dubu = [0]*N
# dubu[M-1] = 3
# sige = M-1
# ban_sige = M-1
# num = 0
# answer = 0
# while True:
#     num += 1
#     sige -= 1
#     ban_sige +=1
#     if sige == -1:
#         sige = N-1
#     if ban_sige == N:
#         ban_sige = 0
#     if 3 - num == K:
#         answer = sige
#         break
#     if 3 + num == K:
#         answer = ban_sige
#         break
# print(answer+1)