# 전화번호 목록
# <해시>
# https://school.programmers.co.kr/learn/courses/30/lessons/42577


# 시간초과 코드

# def solution(phone_book):
#     for phone in phone_book:
#         for phone1 in phone_book:
#             if phone != phone1:
#                 n = len(phone1)
#                 if phone[:n] == phone1:
#                     return False
#
#     return True


# 4번 효율성 실패 코드

# def solution(phone_book):
#     d = dict()
#     for phone in phone_book:
#         d[len(phone)] = d.get(len(phone), [])
#         d[len(phone)].append(phone)
#
#     for j in sorted(d):
#         for p in sorted(phone_book, key=len, reverse=True):
#             if j == len(p):
#                 break
#             for k in d[j]:
#                 if p[:j] == k:
#                     return False
#
#     return True

def solution(phone_book):
    # 정렬(문자열)
    phone_book.sort()
    for i in range(len(phone_book)-1):
        # 현재 문자열 길이 체크
        length = len(phone_book[i])
        # 문자열이므로 비슷한게 모여있음
        # 현재 길이 기준으로 뒤에거만 접두어 확인해줌
        if phone_book[i]== phone_book[i+1][:length]:
            return False

    return True
