a, b = map(int,(input().split()))
c = a * b

while b!=0:
    a = a%b
    a, b = b, a

print(a)
print(c//a)