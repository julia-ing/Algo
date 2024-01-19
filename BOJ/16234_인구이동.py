from collections import deque

N, L, R = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def removeBorder(x, y, visited):
    q = deque([(x, y)])
    visited[x][y] = 1
    united = [(x, y, grid[x][y])]

    while q:
        x, y, = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<N and 0<=ny<N and not visited[nx][ny]:
                if L <= abs(grid[x][y] - grid[nx][ny]) <= R:
                    q.append((nx, ny))
                    visited[nx][ny] = 1
                    united.append((nx, ny, grid[nx][ny]))

    count = len(united)
    if count <= 1:
        return 0
    total = sum(map(lambda x: int(x[2]), united))
    #  분배
    for i, j, num in united:
        grid[i][j] = total // count
    return 1


day = 0
while True:
    visited = [[0]*N for _ in range(N)]
    flag = 0
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                # 모든 위치 연합 체크
                flag += removeBorder(i, j, visited)

    # 연합이 하나도 없으면 종료
    if flag == 0:
        break

    day += 1

print(day)
