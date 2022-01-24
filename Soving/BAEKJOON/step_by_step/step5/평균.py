N = int(input())
scores = list(map(int,input().split()))
m = max(scores)
new = []

for i in scores:
    new.append(i/m * 100)

print(sum(new)/len(new))