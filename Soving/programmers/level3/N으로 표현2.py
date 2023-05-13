def solution(N, number):
    num_set = [set() for _ in range(9)]
    for i in range(9):
        num_set[i].add(int(str(N)*(i+1)))
        for j in range(i):
            for a in num_set[j]:
                for b in num_set[i-j-1]:
                    num_set[i].add(a + b)
                    num_set[i].add(a - b)
                    num_set[i].add(a*b)
                    if b:
                        num_set[i].add(a//b)
        if number in num_set[i]:
            return i+1
    return -1

print(solution(5, 12))