import sys
sys.stdin = open("input.txt", "r")
n = int(input())
planets = list(map(int, input().split()))
max_val = max(planets)

answer = planets[-1]
for i in range(n-2, -1, -1):
    if answer < planets[i]:
        answer = planets[i]
        continue
    if answer%planets[i]:
        answer = (answer//planets[i] + 1) * planets[i]


print(answer)
