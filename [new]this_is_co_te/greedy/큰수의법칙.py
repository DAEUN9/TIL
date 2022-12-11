import sys

sys.stdin = open('input.txt', 'r')

# 배열의 크기, 숫자가 더해지는 횟수, 최대 더하기 횟수
N, M, K = map(int, input().split())
li = list(map(int, input().split()))
li.sort(reverse=True)
def plusNumber():
    total = 0
    cnt = 0
    while cnt<M:
        for i in range(K):
            cnt += 1
            total += li[0]
            if cnt == M:
                return total
        total += li[1]
        cnt += 1
    return total
print(plusNumber())