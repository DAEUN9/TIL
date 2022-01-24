cnt = 0
N = int(input())
for i in range(1,N+1):
    if i < 10:
        cnt+=1
        continue
    li = []
    for j in range(1,len(str(i))):
        a = int(str(i)[j-1])-int(str(i)[j])
        li.append(a)
    se = set(li)
    if len(se) == 1:
        cnt+=1

print(cnt)