def solution(id_list, report, k):
    report = set(report)
    report = list(report)
    list1=[]
    list2=[]
    ind = 0
    cnt = 0
    for re in report:
        a, b = re.split()
        list1.append(b)

    for i in range(len(list1)):
        cnt = 0
        for j in range(i,len(list1)):
            if list1[i]==list1[j]:
                cnt += 1
        if cnt >= k:
            list2.append(list1[i])        
    list2 = set(list2)
    list2 = list(list2)
    list3 = []
    print(list2)
    for r in report:
        c, d = r.split()
        if d in list2:
            list3.append(c)
            
    answer = []
    for id in id_list:
        count = 0
        for n in list3:
            if id ==n:
                count += 1
        answer.append(count)
        
    return answer