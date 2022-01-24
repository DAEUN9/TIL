se = set()
for i in range(10):
    a = int(input())
    b = a%42
    se.add(b)
print(len(se))