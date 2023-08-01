import sys
sys.stdin = open("input.txt", "r")

T = int(input())
d = dict()
d[0] = "{}"
answer = dict()
answer["{}"] = 0
for i in range(1, 16):
    d[i] = "{"
    for j in range(i):
        l = d.get(j, "")
        d[i] += l
        if i-1 != j:
            d[i] += ","
    d[i] += "}"
    answer[d[i]] = i

for _ in range(T):
    A = input()
    B = input()
    print(d[answer[A]+answer[B]])