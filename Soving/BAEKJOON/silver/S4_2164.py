from collections import deque
de = deque()

N = int(input())
for i in range(1,N+1):
    de.append(i)

while len(de)>1:
    de.popleft()
    a = de.popleft()
    de.append(a)
print(de[-1])