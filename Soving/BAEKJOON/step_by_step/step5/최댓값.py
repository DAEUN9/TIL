li = []
for i in range(9):
    a = int(input())
    li.append(a)

mn = max(li)
print(mn)
print(li.index(mn)+1)