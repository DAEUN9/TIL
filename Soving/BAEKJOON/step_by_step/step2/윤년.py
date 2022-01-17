A=int(input())
if A%4==0:
    if A%400==0:
        print('1')
    elif A%100!=0:
        print('1')
    else:
        print('0')
else:
    print('0')