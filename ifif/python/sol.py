import sys
sys.stdin = open("input.txt", "r")

while True:
    numbers = input()
    if numbers == "0":
        break
    n = int(numbers[0])
    numbers = numbers.split()[1:]
    numbers.sort()
    a = []
    b = []
    zero_cnt = 0
    idx = 0
    for number in numbers:
        if number == "0":
            zero_cnt += 1
            continue
        if idx%2 == 0:
            a.append(number)
        else:
            b.append(number)
        idx += 1
    if len(a) == len(b):
        a = a[:1] + ["0"]*(zero_cnt//2 + zero_cnt%2) + a[1:]
        b = b[:1] + ["0"]*(zero_cnt//2) + b[1:]
    else:
        a = a[:1] + ["0"]*(zero_cnt//2) + a[1:]
        b = b[:1] + ["0"]*(zero_cnt//2 + zero_cnt%2) + b[1:]
    print(int("".join(a)) + int("".join(b)))