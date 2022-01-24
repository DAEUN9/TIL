from string import ascii_lowercase, ascii_uppercase

S = input()
lower = list(ascii_lowercase)
upper = list(ascii_uppercase)
li1 = []
li2 = []
new =[]

for l in lower:
    n = 0
    n = S.count(l)
    li1.append(n)

for u in upper:
    n = 0
    n = S.count(u)
    li2.append(n)

num = len(lower)
    
for i in range(num):
    c = li1[i] + li2[i]
    new.append(c)

mn = max(new)
inx = new.index(mn)
if new.count(mn) > 1:
    print('?')
else:
    print(upper[inx])


