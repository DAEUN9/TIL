# 직사각형 네개의 합집합의 면적 구하기

se = set()
for i in range(4):
    a, b, c, d = map(int,input().split())
    for x in range(a, c):
        for y in range(b, d):
            se.add((x, y))

print(len(se))