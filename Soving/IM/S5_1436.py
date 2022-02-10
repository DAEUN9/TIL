# 영화감독 숌

answer = []
num = 0
i = 0
while num < 10000:

    a = str(i).count('666')
    if a >= 1:
        num += 1
        answer.append(i)
    i += 1
N = int(input())

print(answer[N-1])