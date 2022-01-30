T = int(input())

def myeng(li, k, n):
    if k == 0:
        return li[-1]
    li2 = [1]
    a = li1[0]
    for i in range(1,n):
        a += li[i]
        li2.append(a)
     
    return myeng(li2, k-1, n)


for t in range(T):
    
    k = int(input())
    n = int(input())
    li1 = [i for i in range(1, n+1)]
    print(myeng(li1, k, n))
