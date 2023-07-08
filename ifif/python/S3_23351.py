import sys
sys.stdin = open("input.txt", "r")
N, K, A, B = map(int, input().split())

water = [K]*N

def solution():
    day = 0
    while True:
        day += 1
        for i in range(A):
            water[i] += B
        for j in range(N):
            water[j] -= 1
            if not water[j]:
                return day
        water.sort()
print(solution())