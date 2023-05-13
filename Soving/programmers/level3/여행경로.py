def solution(tickets):
    tickets.sort()
    lines = dict()
    answer = ["ICN"]
    visited = dict()
    for a, b in tickets:
        temp = lines.get(a, [])
        temp2 = visited.get(a, [])
        lines[a] = temp + [b]
        visited[a] = temp2 + [0]
        lines[a].sort()
        
        
    q = ["ICN"]
    while q:
        curr = q.pop()
        if lines.get(curr, 0) == 0:
            continue
        for i in range(len(lines[curr])):
            if visited[curr][i]:
                continue
            visited[curr][i] = 1
            answer.append(lines[curr][i])
            q.append(lines[curr][i])
    return answer