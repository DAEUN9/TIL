import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
li = list(map(int, input().split()))
li2 = sorted(li)
d = {
    li2[0]:0
}
before = li2[0]
cnt = 0
for i in range(1, N):
    if before<li2[i]:
        cnt += 1
        before = li2[i]
        a = d.get(li2[i], 0)
        d[li2[i]] = cnt
for l in li:
    print(d[l], end=' ')