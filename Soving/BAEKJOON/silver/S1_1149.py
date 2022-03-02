# import sys
#
# sys.stdin = open('input.txt', 'r')

N = int(input())
roofs = [list(map(int, input().split())) for n in range(N)]

for n in range(1,N):
    for i in range(3):
        roofs[n][i] += min(roofs[n-1][:i]+roofs[n-1][i+1:])
print(min(roofs[-1]))