from string import ascii_lowercase

S = input()
alpha = list(ascii_lowercase)
for i in alpha:
    print(S.find(i),end=' ')