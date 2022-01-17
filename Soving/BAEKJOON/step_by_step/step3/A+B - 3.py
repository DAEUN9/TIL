n=int(input())
pluslist=[]
for i in range(0,n):
    A,B=map(int,input().split())
    pluslist.append(A+B)
for j in range(0,n):
    print(pluslist[0+j])