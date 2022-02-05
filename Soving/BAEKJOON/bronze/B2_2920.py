li = list(map(int, input().split()))

a = li[0]
answer = 'mixed'
if a == 8:
    for l in li[1:]:
        if a -1 == l:
            a = l
        else:
            break
    else:
        answer = 'descending'
elif a == 1:
    for l in li[1:]:
        if a +1 == l:
            a = l
        else:
            break
    else:
        answer = 'ascending'
print(answer)