N = int(input())
total = 0
answer = []
for i in range(N):
    n = 0
    total = 0
    ox = input()
    for j in ox:
        if j == 'O':
            n += 1
            total += n
        else:
            n = 0
    answer.append(total)
for a in answer:
    print(a)