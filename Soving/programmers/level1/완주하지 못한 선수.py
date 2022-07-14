def solution(participant, completion):
    # 참가 선수 딕셔너리
    d = dict()

    # 완주 선수 딕셔너리
    di = dict()

    # 선수별 참가횟수 구하기
    # 완주 선수에 참가선수 추가해주기
    for c in participant:
        d[c] = d.get(c, 0) + 1
        di[c] = di.get(c, 0)

    # 완주 선수 등록
    for a in completion:
        di[a] += 1

    # 참가선수 카운팅과 완주선수 카운팅 안맞으면 return
    for com in participant:
        if d[com] != di[com]:
            return com