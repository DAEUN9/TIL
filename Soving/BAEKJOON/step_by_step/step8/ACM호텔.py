# H, W, N : 층 수, 각층의 방 수, 몇번째 손님
T = int(input())
answer = []
for n in range(T):
    H, W, N = map(int,input().split())
    f = N%H
    if N%H == 0:
        ho = N//H
        f = H
    else:
        ho = N//H+1
    ho = str(ho)
    f = str(f)
    if len(ho)==1:
        ho = '0'+ho
    answer += [f+ho]
for an in answer:
    print(an)
    