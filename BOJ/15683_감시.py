import copy
from itertools import product
import sys

input = sys.stdin.readline
N, M = map(int, input().split())

grid = [list(map(int, input().split())) for _ in range(N)]
# 북동남서
dx = [-1,0,1,0]
dy = [0,1,0,-1]

direction = {
    1: [[0],[1],[2],[3]],
    2: [[0,2],[1,3]],
    3: [[0,1],[1,2],[2,3],[0,3]],
    4: [[0,1,2],[1,2,3],[2,3,0],[3,0,1]],
    5: [[0,1,2,3]]
}

# cctv 정보 저장
cctv = []
blind = 0
for i in range(N):
    for j in range(M):
        if 0 < grid[i][j] < 6:
            cctv.append((grid[i][j], i, j))
        elif grid[i][j] == 0:
            blind += 1

# 모든 cctv 방향의 경우의 수
all_cctv_dir = []
for (num, x, y) in cctv:
    all_cctv_dir.append(direction[num])


def countWatched(temp_grid):
    res = 0
    for i in range(N):
        for j in range(M):
            if temp_grid[i][j] == '#':
                res += 1
    return res

def watch(cctv_dir):
    temp_grid = copy.deepcopy(grid)
    for i, (num, x, y) in enumerate(cctv):
        # i번째 cctv 의 방향
        dir = cctv_dir[i]
        # 마킹
        for d in dir:
            nx, ny = x, y
            while True:
                nx += dx[d]
                ny += dy[d]
                if 0<=nx<N and 0<=ny<M:
                    if temp_grid[nx][ny] == 0:
                        temp_grid[nx][ny] = '#'
                    elif temp_grid[nx][ny] == 6: # 벽
                        break
                else:
                    break
    # 해당 direction set 에서 감시된 개수 카운트
    return countWatched(temp_grid)


possible = []
for cctv_dir in list(product(*all_cctv_dir)):
    possible.append(blind - watch(cctv_dir))

print(min(possible))
