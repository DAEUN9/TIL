import sys
sys.stdin = open("input.txt")

while True:
    temp = input()
    if temp == "0":
        break
    numbers = list(temp.split())
    N = numbers[0]
    numbers = numbers[1:]
    numbers.sort()
    a, b = [], []
    zeros = 0
    i = 0
    for number in numbers:
        if number == "0":
            zeros += 1
            continue
        if i%2 == 0:
            a.append(number)
        if i%2:
            b.append(number)
        i += 1
    if len(a) > len(b):
        a = a[:1] + ["0"] * (zeros // 2) + a[1:]
        b = b[:1] + ["0"] * (zeros // 2 + zeros % 2) + b[1:]
    else:
        a = a[:1] + ["0"] * (zeros//2 + zeros%2) + a[1:]
        b = b[:1] + ["0"] * (zeros//2) + b[1:]
    print(int(''.join(a)) + int(''.join(b)))