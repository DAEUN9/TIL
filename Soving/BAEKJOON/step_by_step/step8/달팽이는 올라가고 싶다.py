A, B, V = map(int,input().split())
a = (V-A)//(A-B)
if (V-A)%(A-B) == 0:
    print(a+1)
else:
    print(a+2)