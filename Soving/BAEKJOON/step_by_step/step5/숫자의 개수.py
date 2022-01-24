A = int(input())
B = int(input())
C = int(input())

li = [str(j) for j in range(10)]
num = str(A*B*C)
for i in li:
    a = num.count(i)
    print(a)