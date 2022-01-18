num = int(input())
count = 0
tmp = num
while True:
    po_num = tmp//10 + tmp%10 #2 + 6
    new = (tmp%10)*10 + po_num%10 # 60 + 8
    count += 1
    if new == num:
        break
    tmp = new
print(count)