import sys
from collections import deque
sys.stdin = open("input.txt", "r")

input = sys.stdin.readline
N = int(input())
dq = deque()
st = []
for _ in range(N):
    req = input().strip("\n")
    if len(req) == 1:
        if st and st[-1] == "1":
            st.pop()
            dq.pop()
        elif st:
            st.pop()
            dq.popleft()
    else:
        comm, alpha = req.split()
        if comm == "1":
            dq.append(alpha)
            st.append(comm)
        else:
            dq.appendleft(alpha)
            st.append(comm)
if dq:
    print("".join(dq))
else:
    print(0)