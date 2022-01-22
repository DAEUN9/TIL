def solution(id_list, report, k):
    repor=set(report)
    repor=list(repor)
    dic_1 = {} #신고 받은사람 key
    for i in id_list:
        dic_1[i]=[]
        
    for re in repor:
        a, b = re.split()
        c = dic_1.get(b)
        c.append(a)
        dic_1[b] = c
    
    list1=[]
    for r in id_list:
        if len(dic_1.get(r)) >= k:
            list1.append(r)
    
    dic_2 = {}
    answer = []

    for id_ in id_list:
        cnt = 0
        for li in list1:
            if id_ in dic_1.get(li):
                cnt += 1
        dic_2[id_] = cnt

    for dd in id_list:
        num = dic_2.get(dd)
        answer.append(num)
        
    return answer