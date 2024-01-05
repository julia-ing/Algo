import sys
from collections import deque
m,n = map(int, sys.stdin.readline().split())

q = deque()
board = []
dx = [-1,1,0,0]
dy = [0,0,-1,1]
answer = 0

for i in range(n):
    board.append(list(map(int, sys.stdin.readline().split())))

for i in range(n):
    for j in range(m):
        if board[i][j] == 1:
            q.append((i,j))

while q:
    x, y = q.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0<=nx<n and 0<=ny<m and board[nx][ny] == 0:
            board[nx][ny] = board[x][y] + 1
            q.append((nx, ny))

for i in range(n):
    for j in range(m):
        if board[i][j] == 0:
            print(-1)
            exit(0)

answer = [max(board[i]) for i in range(n)]
print(max(answer) - 1)
