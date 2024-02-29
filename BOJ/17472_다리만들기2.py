from collections import deque

N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 섬 번호 부여하기
def bfs(x, y, num):
    q = deque()
    q.append((x, y))
    visited[x][y] = 1
    grid[x][y] = num
    
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<N and 0<=ny<M and not visited[nx][ny] and grid[nx][ny] != 0:
                visited[nx][ny] = 1
                grid[nx][ny] = num
                q.append((nx, ny))

visited = [[0]*M for _ in range(N)]
num = 1
for i in range(N):
    for j in range(M):
        if grid[i][j] and not visited[i][j]:
            bfs(i, j, num)
            num += 1

connection = set()
# 이을 수 있는 섬 정보 저장하기
def get_possible_connection(x, y, num):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        dist = 0
        arrived_island = 0
        
        while True:
            # 좌표 범위 벗어남
            if nx<0 or nx>=N or ny<0 or ny>=M:
                break
            # 같은 번호 섬이 있으먄
            if grid[nx][ny] == num:
                break
            # 다른 섬에 속한 땅이면 기록하고 break
            if grid[nx][ny] and grid[nx][ny] != num:
                arrived_island = grid[nx][ny]
                break
            
            nx += dx[i]
            ny += dy[i]
            dist += 1
        
        if dist >= 2 and arrived_island != 0:
            connection.add((num, arrived_island, dist))

for i in range(N):
    for j in range(M):
        if grid[i][j]:
            get_possible_connection(i, j, grid[i][j])

connection = list(connection)
connection.sort(key=lambda x: x[2])

# 크루스칼: 모든 정점을 잇는 최소신장트리 찾기
parent = [i for i in range(num)]
def find(parent, x):
    if x != parent[x]:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

res = 0
connected = 0
for a, b, cost in connection:
    if find(parent, a) != find(parent, b):
        res += cost
        connected += 1
        union(parent, a, b)

if res == 0 or connected != num-2:
    print(-1)
else:
    print(res)
