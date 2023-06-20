import sys
sys.stdin = open("input.txt", "r")

def str_to_minuts(t):
    return int(t[:2])*60 + int(t[2:])
N = int(input())
plays = [input().split() for _ in range(N)]
plays.sort()
end = 600
start = 0
answer = 0
for s, e in plays:
    if str_to_minuts(e)+10 > end:
        answer = max(answer, str_to_minuts(s) - 10 - end)
        end = str_to_minuts(e)+10
answer = max(22*60 - end, answer)
print(answer)
