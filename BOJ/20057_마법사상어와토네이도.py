# 해답 참고 - 다시 풀어보기
N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]

# 방향별 모래
left = [(1, 1, 0.01), (-1, 1, 0.01), (1, 0, 0.07), (-1, 0, 0.07), (1, -1, 0.1),
         (-1, -1, 0.1), (2, 0, 0.02), (-2, 0, 0.02), (0, -2, 0.05), (0, -1, 0)]
right = [(x, -y, z) for x, y, z in left]
down = [(-y, x, z) for x, y, z in left]
up = [(y, x, z) for x, y, z in left]


def calculate(n, percentage, dx, dy):   
    global sx, sy, res
    for _ in range(n):
        sx += dx
        sy += dy
        if sy < 0:
            break
        total = 0
        for dx, dy, per in percentage:
            nx = sx + dx
            ny = sy + dy
            if per == 0: # 알파, 나머지
                new = grid[sx][sy] - total
            else:
                new = int(grid[sx][sy] * per)
                total += new
            if 0 <= nx < N and 0 <= ny < N:
                grid[nx][ny] += new
            else:
                res += new

res = 0
sx, sy = N//2, N//2  # 가운데부터 시작

for n in range(1, N + 1):
    if n % 2 == 0:
        # 오른, 위
        calculate(n, right, 0, 1)
        calculate(n, up, -1, 0)
    else:
        # 왼, 아래
        calculate(n, left, 0, -1)
        calculate(n, down, 1, 0)

print(res)
