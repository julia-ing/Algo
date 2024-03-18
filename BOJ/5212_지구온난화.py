import copy

R, C = map(int, input().split())
grid = [list(input()) for _ in range(R)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def check(x, y):
    count = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<R and 0<=ny<C:
            if grid[nx][ny] == '.':
                count += 1
        else:
            # 범위를 벗어나면 바다
            count += 1
    return count

# 해수면 상승
new_grid = copy.deepcopy(grid)
for i in range(R):
    for j in range(C):
        if grid[i][j] == 'X':
            if check(i, j) >= 3:
                new_grid[i][j] = '.'

# 지도 크기는 모든 섬을 포함하는 가장 작은 직사각형
min_x, min_y = R, C
max_x, max_y = 0, 0
for r in range(R):
    for c in range(C):
        if new_grid[r][c] == 'X':
            min_x = min(min_x, r)
            min_y = min(min_y, c)
            max_x = max(max_x, r)
            max_y = max(max_y, c)

for x in range(min_x, max_x+1):
    for y in range(min_y, max_y+1):
        print(new_grid[x][y], end='')
    print()
