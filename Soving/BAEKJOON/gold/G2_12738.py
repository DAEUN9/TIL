import sys
sys.stdin = open("input.txt", "r")

N = int(input())
li = list(map(int, input().split()))
parts = [li[0]]
def binary_search(start, end, target):
    if start > end:
        return start
    curr = (start+end)//2
    if parts[curr] == target:
        return curr
    if parts[curr] > target:
        return binary_search(start, curr-1, target)
    else:
        return binary_search(curr+1, end, target)

for i in range(1, N):
    if parts[-1] < li[i]:
        parts.append(li[i])
    else:
        idx = binary_search(0, len(parts)-1, li[i])
        parts[idx] = li[i]
print(len(parts))