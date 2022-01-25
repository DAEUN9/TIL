li = ['c=', 'c-', 'dz=', 'd-','lj','nj','s=','z=']
S = input()

   
for i in li:
    S = S.replace(i,'!')

answer = len(S)
print(answer)