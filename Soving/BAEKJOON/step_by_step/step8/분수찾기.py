N = int(input())
n = 0
seq = 0
while n < N:
    seq +=1
    n += seq
    
n = (n - seq)
if seq%2 == 0:
    a = 1
    b = seq
    for i in range(n+1, N):
        a += 1
        b -= 1
else:
    a = seq
    b = 1
    for i in range(n+1, N):
        a -= 1
        b += 1
print(str(a)+'/'+str(b))

