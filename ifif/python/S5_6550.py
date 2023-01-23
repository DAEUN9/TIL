import sys
sys.stdin = open("input.txt", "r")


while True:
    try:
        wordA, wordB = input().split()
    except:
        break

    idx = 0
    for alphabet in wordB:
        if alphabet == wordA[idx]:
            idx +=1
        if idx == len(wordA):
            print("Yes")
            break
    else:
        print("No")
