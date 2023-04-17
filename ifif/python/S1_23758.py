import heapq
import sys
sys.stdin = open("input.txt", "r")
N = int(input())
numbers = list(map(int, input().split()))
numbers.sort()
numbers1 = []
for i in range(N//2):
    heapq.heappush(numbers1, -numbers[i])
numbers2 = numbers[N//2:]
temp1, temp2 = numbers[N//2], numbers[N//2]
cnt = 0
while temp1//2 !=0:
    cnt += 1
    temp1 = heapq.heappop(numbers1)
    heapq.heappush(numbers2, -temp1//2)
    temp2 = heapq.heappop(numbers2)
    heapq.heappush(numbers1, -temp2)
print(cnt)