def solution(board, skill):
    answer = 0
    cal = [[0]*(len(board[0])+1) for _ in range(len(board) + 1)]
    for type, r1, c1, r2, c2, degree in skill:
        if type == 1:
            degree *= -1
        cal[r1][c1] += degree
        cal[r1][c2+1] -= degree
        cal[r2+1][c1] -= degree
        cal[r2+1][c2+1] += degree
        
    for r in range(len(board)+1):
        for c in range(1, len(board[0])+1):
            cal[r][c] += cal[r][c-1]
            
    for c in range(len(board[0])+1):
        for r in range(1, len(board)+1):
            cal[r][c] += cal[r-1][c]
            
    for r in range(len(board)):
        for c in range(len(board[0])):
            if board[r][c] + cal[r][c] > 0:
                answer += 1
    return answer