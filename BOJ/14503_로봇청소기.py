N, M = map(int, input().split())
sx, sy, sd = map(int, input().split())

grid = [list(map(int, input().split())) for _ in range(N)]

# 북, 동, 남, 서 (시계 방향)
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def dfs(x, y, d):
    global res
    if grid[x][y] == 0:
        grid[x][y] = 2
        res += 1
    for _ in range(4):
        nd = (d + 3) % 4  # 반시계
        nx = x + dx[nd]
        ny = y + dy[nd]
        d = nd
        if 0 <= nx < N and 0 <= ny < M and grid[nx][ny] == 0:
            # 범위 안에 있고 아직 청소를 안한 곳이라면 전진
            dfs(nx, ny, nd)
            return
    # 후진
    nd = (d + 2) % 4
    nx = x + dx[nd]
    ny = y + dy[nd]
    # 벽이면 중단
    if grid[nx][ny] == 1:
        return
    else:
        dfs(nx, ny, d)

res = 0
dfs(sx, sy, sd)

print(res)
