import sys
sys.stdin = open("input.txt", "r")

li = input()

total = int(li[0])
for l in li[1:]:
    curr = int(l)
    if curr <= 1:
        total += curr
    elif total <= 1:
        total += curr
    else:
        total *= curr
print(total)