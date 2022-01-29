# 종이 자르기

w, h = map(int, input().split())
num = int(input())

x_list = [0, h]
y_list = [0, w]
for n in range(num):
    p, dot_num = map(int, input().split())
    if p == 0:
        x_list.append(dot_num)
    else:
        y_list.append(dot_num)
x_list.sort()
y_list.sort()
curr_x = x_list[1] - x_list[0]
curr_y = y_list[1] - y_list[0]

for x in range(2, len(x_list)):
    a = x_list[x] - x_list[x-1]
    if curr_x < a:
        curr_x = a

for y in range(2, len(y_list)):
    b = y_list[y] - y_list[y-1]
    if curr_y < b:
        curr_y = b

print(curr_x * curr_y)

