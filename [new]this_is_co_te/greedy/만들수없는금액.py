# 동전 줄세우기
# 숫자를 차례대로 for문 돌기
# 동전을 차례대로 더해서 목표보다 작으면 넘어감
# 초과되면 num 리턴
import sys
sys.stdin = open("input.txt", "r")

N = int(input())
coins = list(map(int, input().split()))
coins.sort()
num = 1
for coin in coins:
    if num < coin:
        break
    num += coin
print(num)