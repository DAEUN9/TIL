import sys
sys.stdin = open("input.txt", "r")

def time_to_seconds(t):
    m, s = map(int, t.split(":"))
    return m*60+s

def seconds_to_time(t):
    m = str(t//60)
    s = str(t%60)
    return m.zfill(2)+':'+s.zfill(2)

N = int(input())
d = {
    "1":0,
    "2":0
}
answer = [0, 0]
check = 0
for _ in range(N):
    team, time = input().split()
    if d["1"] > d["2"]:
        answer[0] += time_to_seconds(time) - check
    elif d["2"] > d["1"]:
        answer[1] += time_to_seconds(time) - check
    check = time_to_seconds(time)
    d[team] += 1

if d["1"] > d["2"]:
    answer[0] += 48*60 - time_to_seconds(time)
elif d["2"] > d["1"]:
    answer[1] += 48*60 - time_to_seconds(time)

print(seconds_to_time(answer[0]))
print(seconds_to_time(answer[1]))