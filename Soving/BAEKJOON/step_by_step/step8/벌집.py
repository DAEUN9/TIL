N = int(input())
i = 1
num = 1
while True:
    num = num+6*(i-1)
    if num >= N:
        a = i
        break
    i += 1
print(a)
