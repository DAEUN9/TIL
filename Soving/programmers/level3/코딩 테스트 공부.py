def solution(alp, cop, problems):
    max_alp, max_cop = 0, 0
    # 알고요청, 코딩요청, 알고보상, 코딩보상, 시간
    for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
        max_alp = max(alp_req, max_alp)
        max_cop = max(cop_req, max_cop)

    # 이미 알고력과 코딩력이 충분하면 0 return
    if max_alp <= alp and max_cop <= cop:
        return 0

    # [알고력][코딩력]=시간 dp 테이블 생성
    dp = [[1e9] * (max_cop + 1) for _ in range(max_alp + 1)]
    # 알고력이나 코딩력이 req_max값보다 높으면 req_max를 알고력or코딩력으로 정함
    alp, cop = min(alp, max_alp), min(cop, max_cop)
    dp[alp][cop] = 0

    for ma in range(alp, max_alp + 1):
        for mc in range(cop, max_cop + 1):
            # 1의 시간을 써서 알고력or코딩력을 높임
            if ma + 1 <= max_alp:
                dp[ma + 1][mc] = min(dp[ma][mc] + 1, dp[ma + 1][mc])
            if mc + 1 <= max_cop:
                dp[ma][mc + 1] = min(dp[ma][mc] + 1, dp[ma][mc + 1])

            # 문제를 순회하며 현재 알고력(ma), 코딩력(mc)가 요청보다 높으면 dp 갱신
            for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
                if ma >= alp_req and mc >= cop_req:
                    # 범위를 max값으로 제한
                    temp_alp = min(ma + alp_rwd, max_alp)
                    temp_cop = min(mc + cop_rwd, max_cop)
                    # 시간의 최소값을 갱신
                    dp[temp_alp][temp_cop] = min(dp[temp_alp][temp_cop], dp[ma][mc] + cost)
    return dp[-1][-1]
