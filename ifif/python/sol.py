import sys
sys.stdin = open("input.txt", "r")

def str_to_minutes(t):
    h = int(t[:2])
    m = int(t[2:])
    return h*60 + m
N = int(input())
plays = [input().split() for _ in range(N)]
plays.sort()
answer = 0
end = 600
for s, e in plays:
    s = str_to_minutes(s)
    e = str_to_minutes(e)
    if e + 10 > end:
        answer = max(answer, s - 10 - end)
        end = e + 10
answer = max(22*60 - end, answer)
print(answer)