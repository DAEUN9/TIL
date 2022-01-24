a, b = input().split()
c = ''
m = a
for i in range(1,4):
    if a[-i] > b[-i]:
        m = a
        break
    elif a[-i] == b[-i]:
        continue
    else:
        m = b
        break

for j in m:
    c = j + c

print(c)
