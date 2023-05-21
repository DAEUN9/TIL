import sys
sys.stdin = open("input.txt", "r")

formula = list(input())
stack = []
atom_dic = {
    "H" : 1,
    "C" : 12,
    "O" : 16
}
answer = 0
while formula:
    curr = formula.pop(0)
    if curr == ")":
        num = 0
        while stack:
            temp = stack.pop()
            if temp == "(":
                break
            num += temp
        stack.append(num)
    elif curr == "(":
        stack.append(curr)
    elif "1" <= curr <= "9":
        stack[-1] *= int(curr)
    else:
        stack.append(atom_dic[curr])

print(sum(stack))