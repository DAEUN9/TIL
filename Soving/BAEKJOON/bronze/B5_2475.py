li = list(map(int, input().split()))
total = 0
for l in li:
    total += (l**2)
print(total%10)