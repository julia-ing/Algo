import sys
r,c,k = map(int, sys.stdin.readline().split())

board = []
for _ in range(r):
    board.append(list(sys.stdin.readline()))
board[r-1][0] = 'T'

answer = 0
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def backtrack(x, y, step):
    global answer
    if step == k:
        if x == 0 and y == c-1:
            answer += 1
    else:
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<r and 0<=ny<c and board[nx][ny] != 'T':
                board[nx][ny] = 'T'
                backtrack(nx, ny, step+1)
                board[nx][ny] = '.'

backtrack(r-1, 0, 1)
print(answer)
