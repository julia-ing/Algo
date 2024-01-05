from collections import deque

n, m = map(int, input().split())
island = []
for i in range(n):
    island.append(list(input()))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(i, j):
    q = deque()
    q.append((i, j))
    visited=[[0]*m for _ in range(n)]
    visited[i][j] = 1
    dist = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            elif island[nx][ny] == 'L' and visited[nx][ny] == 0:
                visited[nx][ny] = visited[x][y] + 1
                dist = max(dist, visited[nx][ny])
                q.append((nx,ny))
    return dist - 1

result = 0
for i in range(n):
    for j in range(m):
        if island[i][j] == 'L':
            result = max(result, bfs(i,j))

print(result)
