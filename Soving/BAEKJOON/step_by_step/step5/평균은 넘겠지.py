N = int(input())
answer = []
for i in range(N):
    high_li = []
    li = list(map(int,input().split()))[1:]
    a = sum(li)/len(li)
    for j in li:
        if j >a:
            high_li.append(j)
    b = len(high_li)/len(li)*100
    c = f'{len(high_li)/len(li)*100:.3f}'
    answer.append(c)
for an in answer:
    print(an+'%')