n, m = map(int,input().split())

board = []
for i in range(n):
    board.append(list(map(int, input())))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
def dfs(x, y):
    board[x][y] = -1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == 0:
            board[nx][ny] = -1
            dfs(nx, ny)

res = 0
for i in range(n):
    for j in range(m):
        if board[i][j] == 0:
            res += 1
            dfs(i, j)

print(res)
