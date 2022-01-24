se1 = set(range(1,10001))
se2 = set()
for i in range(1,10001):
    total = 0
    for j in str(i):
        total += int(j)
    total += i
    se2.add(total)

answer = se1-se2
answer = list(answer)
answer.sort()
for k in answer:
    print(k)