# 반도체 설계
#
# 이분 탐색
# 가장 긴 증가하는 부분 수열: o(n log n)

import sys
sys.stdin = open("input.txt", "r")
n = int(input())
ports = list(map(int, input().split()))
link_ports = [ports[0]]
answer = 0
def binary_search(start, end, target):
    if start > end:
        return start
    mid = (start+end) // 2

    if link_ports[mid] > target:
        return binary_search(start, mid-1, target)
    elif link_ports[mid] < target:
        return binary_search(mid+1, end, target)
    else:
        return mid

for i in range(1, n):
    if link_ports[-1] < ports[i]:
        link_ports.append(ports[i])
    else:
        curr = binary_search(0, len(link_ports)-1, ports[i])
        link_ports[curr] = ports[i]
print(len(link_ports))