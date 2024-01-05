n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

max_val = max(map(max, board))
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
visited = [[False] * m for _ in range(n)]
answer = 0

def dfs(x, y,  step, total):
    global answer

    if total + max_val*(4-step) <= answer:
        return

    if step == 4:
        answer = max(answer, total)
        return

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<n and 0<=ny<m and not visited[nx][ny]:
            if step == 2:
                visited[nx][ny] = True
                dfs(x, y, step+1, total + board[nx][ny])
                visited[nx][ny] = False
            visited[nx][ny] = True
            dfs(nx, ny, step+1, total + board[nx][ny])
            visited[nx][ny] = False


for i in range(n):
    for j in range(m):
        visited[i][j] = True
        dfs(i, j, 1, board[i][j])
        visited[i][j] = False

print(answer)