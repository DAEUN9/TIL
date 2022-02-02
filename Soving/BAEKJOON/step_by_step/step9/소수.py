start = int(input())
end = int(input())

total = []
for num in range(start, end+1):
    for n in range(2, num+1):
        if n == num:
            total += [num]
        if num%n == 0:            
            break

if total == []:
    print(-1)
else:
    print(sum(total))
    print(total[0])