T = int(input())
li = ['MON','TUE','WED','THU','FRI','SAT','SUN']
answer = []
for i in range(1,T+1):
    S = input()
    b = 0
    if S == 'SUN':
        answer.append(7)
    else:
        b = li.index(S)
        answer.append(6-b)
idx = 1
for j in answer:
    print('#'+str(idx),j)
    idx += 1