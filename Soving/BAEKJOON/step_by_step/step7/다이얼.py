dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']

total = 0
word = input()
for d in dial:
    for w in word:
        if w in d:
            total += dial.index(d)
            total += 3

print(total)