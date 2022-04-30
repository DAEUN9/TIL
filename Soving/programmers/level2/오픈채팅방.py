# https://programmers.co.kr/learn/courses/30/lessons/42888

def solution(record):
    answer = []
    result = []
    d = dict()
    for reco in record:
        recor = reco.split()
        if len(recor) ==3:
            move, user_id, nickname = recor
            d[user_id] = nickname
            if move == 'Enter':
                answer.append((1, user_id))
        else:
            move, user_id = recor
            answer.append((0, user_id))
    for a, id in answer:
        if a:
            result.append(f'{d[id]}님이 들어왔습니다.')
        else:
            result.append(f'{d[id]}님이 나갔습니다.')
    
    return result