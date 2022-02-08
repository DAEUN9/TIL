N = int(input())

for i in range(1, N):
    answer = i
    j = i

    while j >= 1:
        answer += j%10
        j = j//10
    if answer == N:
        answer = i
        break
else:
    answer = 0
print(answer)
