from pprint import pprint
import sys
from collections import deque

sys.setrecursionlimit(1000)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def in_range(x, y):
    return 0<=x<N and 0<=y<M

def dfs(x, y, minus):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 주변에 바다가 있으면
        if in_range(nx, ny) and board[nx][ny] == 0:
            minus[x][y] += 1

def melt():
    # 주변 0개수만큼 빼기, 음수는 없음
    for i in range(1, N-1):
        for j in range(1, M-1):
            if minus[i][j] > 0:
                board[i][j] -= minus[i][j]
                if board[i][j] < 0:
                    board[i][j] = 0

def find_group_bfs(x, y):
    visited[x][y] = 1
    q = deque()
    q.append((x, y))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if in_range(nx, ny):
                if not visited[nx][ny] and board[nx][ny] > 0:
                    visited[nx][ny] = 1
                    q.append((nx, ny))


N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

res = 1
while True:
    minus = [[0] * M for _ in range(N)]
    for i in range(1, N-1):
        for j in range(1, M-1):
            if board[i][j] > 0:
                # 주변 바다 개수 (빼야 할 개수) 구하기
                dfs(i, j, minus)
    # 얼음 녹임
    melt()
    
    # 그룹 탐색
    visited = [[0] * M for _ in range(N)]
    ice = 0
    for i in range(1, N-1):
        for j in range(1, M-1):
            if not visited[i][j] and board[i][j] > 0:
                find_group_bfs(i, j)
                ice += 1

    if ice == 0:
        print(0)
        exit(0)
    # 빙산 2개 이상이면 리턴
    if ice >= 2:
        break
    res += 1

print(res)
