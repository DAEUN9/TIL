N = int(input())
num_li = list(map(int, input().split()))
cnt = 0
for num in num_li:
    for n in range(2, num):
        if num%n == 0:
            break
    else:
        cnt += 1
    if num == 1:
        cnt -= 1
print(cnt)