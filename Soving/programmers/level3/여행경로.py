def solution(tickets):
    tickets.sort()
    lines = dict()
    answer = []
    for a, b in tickets:
        temp1 = lines.get(a, [])
        temp1.append([b, 0])
        lines[a] = temp1

    def dfs(curr, cnt, temp):
        if cnt == len(tickets)+1:
            answer.append(temp)
            return
        if lines.get(curr, 0) == 0:
            return
        for l in range(len(lines[curr])):
            if lines[curr][l][1]:
                continue
            lines[curr][l][1] = 1
            dfs(lines[curr][l][0], cnt + 1, temp + [lines[curr][l][0]])
            lines[curr][l][1] = 0

    dfs("ICN", 1, ["ICN"])
    answer.sort()
    return answer[0]

print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]))