# 효율성 실패 코드
# def solution(board, skill):
#     cnt = 0
#     for s in skill:
#         for r in range(s[1], s[3]+1):
#             for c in range(s[2], s[4]+1):
#                 if s[0] == 1:
#                     board[r][c] -= s[5]
#                 else:
#                     board[r][c] += s[5]
                    
#     for i in range(len(board)):
#         for j in range(len(board[0])):
#             if board[i][j] > 0:
#                 cnt += 1
                    
#     return cnt
        
# 2번 솔루션: 누적힙
def solution(board, skill):
    answer = 0
    tmp = [[0]*(len(board[0])+1) for _ in range(len(board)+1)]
    for s in skill:
        t, r1, c1, r2, c2, d = s
        if t == 1:
            d = -d
        tmp[r1][c1] += d
        tmp[r1][c2+1] -=d
        tmp[r2+1][c1] -=d
        tmp[r2+1][c2+1] +=d
    
    # 행 기준 누적합
    for i in range(len(tmp)-1):
        for j in range(len(tmp[0])-1):
            tmp[i][j+1] += tmp[i][j]
            
    # 열 기준 누적합
    for j in range(len(tmp[0])-1):
        for i in range(len(tmp)-1):
            tmp[i+1][j] += tmp[i][j]
    
    # 누적합 합하기
    for i in range(len(board)):
        for j in range(len(board[0])):
            board[i][j] += tmp[i][j]
            if board[i][j] > 0:
                answer += 1
    
    return answer
