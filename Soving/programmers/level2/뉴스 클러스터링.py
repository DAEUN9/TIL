
d1 = dict()
d2 = dict()

def solution(str1, str2):
    answer = 0
    intersection = 0
    union = 0
    str_1, str_2 = list(str1), list(str2)
    li_1, li_2 = make_two(str_1), make_two(str_2)
    
    for a in li_1:
        cnt = d1.get(a, 0)
        d1[a] = cnt+1
        
    for a in li_2:
        cnt = d2.get(a, 0)
        d2[a] = cnt+1

    for key in list(set(list(d1.keys()) + list(d2.keys()))):
        cnt1, cnt2 = d1.get(key, 0), d2.get(key, 0)
        union += max(cnt1, cnt2)
        intersection += min(cnt1, cnt2)
        
    if not union:
        return 65536
    return int((intersection/union) * 65536)

def to_correct(s):
    o = ord(s)
    if 65 <= o <= 90:
        return s
    elif 97 <= o <= 122:
        return chr(o-32)
    return False

def make_two(li):
    result = []
    for i in range(len(li)-1):
        a, b = to_correct(li[i]), to_correct(li[i+1])
        if a and b:
            result.append(tuple([a, b]))
    return result

        