import sys
from collections import Counter
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
K, L = map(int ,input().split())
answer = []
students = [input().strip() for _ in range(L)]
counter = Counter(students)
d = dict()
for l in students:
    d[l] = d.get(l, 0) + 1
    if counter[l] == d[l]:
        answer.append(l)
for a in answer[:K]:
    print(a)