from collections import deque

n = int(input())
ice = [list(input()) for _ in range(n)]
visited = [[0] * n for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    area, perimeter = 1, 0

    q = deque()
    q.append((x, y))
    visited[x][y] = 1

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n or ice[nx][ny] == ".":
                perimeter += 1
            elif not visited[nx][ny]:
                area += 1
                visited[nx][ny] = 1
                q.append((nx, ny))
    return area, perimeter

max_area = 0
min_perimeter = 1e9

for i in range(n):
    for j in range(n):
        if ice[i][j] == "#" and not visited[i][j]:
            area, perimeter = bfs(i, j)

            if area > max_area:
                max_area, min_perimeter = area, perimeter
            elif area == max_area:
                if perimeter < min_perimeter:
                    max_area, min_perimeter = area, perimeter

print(max_area, min_perimeter)
