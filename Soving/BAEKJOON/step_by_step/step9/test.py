start = int(input())
end = int(input())
answer = 0
total = []
minimum = start
for num in range(start, end+1):
    for n in range(2, num):
        if num%n == 0:            
            break
    else:
        total += [num]
        answer += num
    if num == 1:
        total -= [1]
if total == []:
    print(-1)
else:
    print(answer)
    print(total[0])