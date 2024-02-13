from collections import deque

H, W = map(int, input().split())
level = list(map(int, input().split()))

grid = [[0]*W for _ in range(H)]

for col in range(W):
    for i in range(level[col]):
        grid[H-i-1][col] = 1

visited = [[0]*W for _ in range(H)]

def bfs(nxt, x, y):
    grid[x][y] = 2
    q = deque()
    q.append((x, y))
    visited[x][y] = 1
    
    while q:
        x, y = q.popleft()
        ny = y + nxt
        if 0<ny<W and not visited[x][ny]:
            if grid[x][ny] == 0:
                grid[x][ny] = 2
                q.append((x, ny))

for i in range(H):
    for j in range(W):
        # 만약에 블록이 없는데 끝에가 비어있으면, 양옆으로 탐색하며 비어있는 값을 임의의 값으로 채워줌
        if grid[i][j] == 0:
            if j == 0:
                bfs(1, i, j)  # 왼쪽 끝이면 오른쪽으로 탐색
            elif j == W-1:
                bfs(-1, i, j)  # 오른쪽 끝이면 왼쪽으로 탐색

res = 0
for i in range(H):
    for j in range(W):
        if grid[i][j] == 0:
            res += 1

print(res)


# 풀이 2: 스터디하면서 아이디어 얻음
# res = 0
# for level in range(H):
#     idx = []
#     for v in range(W):
#         if grid[level][v] == 1:
#             idx.append(v)

#     for i in range(len(idx)-1):
#         if idx[i+1] - idx[i] > 1:
#             res += idx[i+1] - idx[i] - 1
# print(res)