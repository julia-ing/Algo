from collections import deque

M, N, K = map(int, input().split())
grid = [[0] * N for _ in range(M)]

# 직사각형 정보로 grid 채우기
for _ in range(K):
    lx, ly, rx, ry = map(int, input().split())
    for i in range(ly, ry):
        for j in range(lx, rx):
            grid[i][j] += 1

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 영역 구하기 위한 bfs 함수
def bfs(x, y):
    total = 1  # 영역 넓이
    q = deque()
    q.append((x, y))
    
    grid[x][y] = -1
    
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0<=nx<M and 0<=ny<N and grid[nx][ny] == 0:
                grid[nx][ny] = -1
                total += 1
                q.append((nx, ny))
              
    return total
    
# 0인 경우 bfs 모두 부르고 영역 넓이 저장
res = []
for i in range(M):
    for j in range(N):
        if grid[i][j] == 0:
            res.append(bfs(i, j))

print(len(res))
res.sort()
print(*res)