# 수학
# 문자열
# 그리디 알고리즘
# 정렬
# 정수론

# 30

import sys
sys.stdin = open("input.txt", "r")

N = list(input())
numbers = N[:]
N = list(map(int, N))
numbers.sort(reverse=True)
end = int(''.join(numbers))

if sum(N)%3 == 0:
    if end%10 == 0:
        print(end)
    else:
        print(-1)
else:
    print(-1)

