import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
N, M = map(int, input().split())
girl_group = dict()
for _ in range(N):
    group = input().strip()
    member_cnt = int(input())
    girl_group[group] = []
    for _ in range(member_cnt):
        girl_group[group].append(input().strip())
for _ in range(M):
    name = input().strip()
    option = int(input())
    if option:
        for k, v in girl_group.items():
            if name in v:
                print(k)
                break
    else:
        print(*sorted(girl_group[name]), sep="\n")