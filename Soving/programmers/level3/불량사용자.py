from itertools import combinations

def solution(user_id, banned_id):
    answer = 0
    ban_cnt = len(banned_id)
    match = dict()
    for ban in banned_id:
        for user in user_id:
            if check_include(ban, user):
                match[ban] = match.get(ban, set())
                match[ban].add(user)
    print(set(combinations(user_id, 3)))
    return answer

def check_include(ban, user):
    if len(ban) != len(user):
        return False
    for a, b in zip(ban, user):
        if a == "*":
            continue
        if a!=b:
            return False
    return True