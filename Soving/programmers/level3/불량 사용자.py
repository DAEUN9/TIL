from itertools import permutations

def solution(user_id, banned_id):
    answer = []
    ban_cnt = len(banned_id)
    for users in permutations(user_id, ban_cnt):
        temp_cnt = 0
        for user, ban in zip(users, banned_id):
            if check_match(ban, user):
                temp_cnt += 1
        if temp_cnt == ban_cnt and set(users) not in answer:
            answer.append((set(users)))
    print(answer)
    return len(answer)

def check_match(ban, user):
    if len(ban) != len(user):
        return False
    for a, b in zip(ban, user):
        if a == "*":
            continue
        if a!=b:
            return False
    return True