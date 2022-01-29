# 창고 다각형

num = int(input())
sticks = []
high_x = 0
high_y = 0
for n in range(num):
    x, y = map(int,input().split())
    sticks.append((x, y))
    sticks.append((x+1, y))
    if y > high_y:
        high_y = y
        high_x = x
sticks = set(sticks)
sticks = list(sticks)
sticks.sort()
curr = 0
dot_li = []
for stick in sticks:
    a = stick[1]
    if curr <= a:
        if a == high_y:
            if len(dot_li) > 0:
                dot_li.append((stick[0], dot_li[-1][1]))
        dot_li.append(stick)
        curr = a
print(dot_li)
sticks.reverse()
curr = 0
dot_li2=[]

for stic in sticks:
    if stic[0] > high_x:
        b = stic[1]
        if curr <= b:
            if b == high_y:
                break
            dot_li2.append(stic)
            curr = b
dot_li2.sort()
if len(dot_li2) > 1:
    dot_li2.insert(0, (dot_li[-1][0], dot_li2[-1][1]))
dot_li.extend(dot_li2)
answer = 0
for i in range(len(dot_li)-1):
    xw = abs(dot_li[i+1][0] - dot_li[i][0])
    answer += xw*dot_li[i][1]
print(answer)
