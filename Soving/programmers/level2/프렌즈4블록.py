def solution(m, n, board):
    visited = []
    answer = 0
    for j in range(n):
        temp = []
        for i in range(m):
            temp = [[board[i][j], 0]] + temp
        visited.append(temp)
    flag = True
    while flag:
        flag = False
        for i in range(n-1):
            for j in range(m-1):
                if (visited[i][j] and visited[i+1][j] and visited[i+1][j+1] and visited[i][j+1]) and (visited[i][j][0] == visited[i+1][j][0] == visited[i+1][j+1][0] == visited[i][j+1][0]):
                    visited[i][j][1] = visited[i+1][j][1] = visited[i+1][j+1][1] = visited[i][j+1][1] = 1
                    flag = True
        while True:
            move = 0
            for i in range(n):
                for j in range(m):
                    if visited[i][j] and visited[i][j][1]:
                        move = 1
                        answer += 1
                        visited[i].pop(j)
                        visited[i].append([])
            if not move:
                break
        
    return answer