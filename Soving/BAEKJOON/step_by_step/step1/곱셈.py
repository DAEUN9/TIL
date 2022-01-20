A=int(input())
B=input()
result=0
position=0
for i in reversed(B):
    curr=int(i)*A
    print(curr)
    result+=curr*10**position
    position+=1
print(result)