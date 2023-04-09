import sys
sys.stdin = open("input.txt", "r")
N, K = map(int, input().split())
per_li = [str(i) for i in range(1, N+1)]
answer = []
before = -1
while per_li:
    idx = (K+before)%len(per_li)
    curr = per_li.pop(idx)
    answer.append(curr)
    before = idx-1
print('<'+', '.join(answer)+'>')