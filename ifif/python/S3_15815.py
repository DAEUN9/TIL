import sys
sys.stdin = open("input.txt", "r")
S = list(input())
stack = []
for s in S:
    if "0" <= s <= "9":
        stack.append(int(s))
        continue
    a = stack.pop()
    b = stack.pop()
    if s == "*":
        stack.append(a*b)
    elif s == "/":
        stack.append(b//a)
    elif s == "+":
        stack.append(a+b)
    else:
        stack.append(b-a)
print(stack[0])



