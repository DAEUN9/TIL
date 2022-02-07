# 팰린드롬수

while True:
    word = input()
    if word == '0':
        break
    answer = 'yes'
    for i in range(len(word)//2):
        if word[i]==word[-1-i]:
            continue
        answer = 'no'
        break
    if word[0] == '0':
        answer = 'no'

    print(answer)