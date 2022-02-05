while True:
    li = list(map(int,input().split()))
    if li==[0,0,0]:
        break
    z = max(li)
    li.remove(z)
    total = 0
    for i in li:
        total += i**2
    if total == z**2:
        print("right")
    else:
        print("wrong")
