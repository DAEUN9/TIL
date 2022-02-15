
li = [1] * 10

N= int(input())

for i in range(N-1):
    for j in range(1, 10):
        li[j] += li[j-1]

print(sum(li)%10007)
