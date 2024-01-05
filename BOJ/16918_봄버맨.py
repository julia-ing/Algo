import sys
from collections import deque
r, c, n = map(int, sys.stdin.readline().split())

board = []
bomb = deque()

dx = [-1,1,0,0]
dy = [0,0,-1,1]

for i in range(r):
    board.append(list(input()))

# 폭탄 폭발
def bfs(q,board):
    while q:
        x,y = q.popleft()
        board[x][y] = '.'
        for i in range(4):
            nx,ny = x+dx[i],y+dy[i]
            if 0<=nx<r and 0<=ny<c and board[nx][ny] =='O':
                board[nx][ny] = '.'

def solve(t):
    global bomb, board
    if t == 1:
        for i in range(r):
            for j in range(c):
                if board[i][j] == 'O':
                    bomb.append((i, j))
    elif t%2 == 1:
        # 3초 지난 폭탄 폭발
        bfs(bomb, board)
        # 3초 후 터질 폭탄 저장
        for i in range(r):
            for j in range(c):
                if board[i][j] == 'O':
                    bomb.append((i, j))

    else:
        board = [['O']*c for _ in range(r)]

for i in range(1, n+1):
    solve(i)

for i in board:
    print(''.join(i))
