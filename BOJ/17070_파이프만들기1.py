import sys
input = sys.stdin.readline
n = int(input())
house = [list(map(int, input().split())) for _ in range(n)]

if house[n-1][n-1] == 1:
    print(0)
    exit(0)

def in_range(x, y):
    return 0<=x<n and 0<=y<n

# d - [0:가로, 1:세로, 2:대각선]
res = 0
def dfs(x2, y2, d):
    global res
    if x2 == n-1 and y2 == n-1:
        res += 1
    
    # 현재 가로나 대각선이면, 옆으로 밀 수 있음
    if d == 0 or d == 2:
        ny2 = y2 + 1
        if in_range(x2, ny2) and house[x2][ny2] != 1:
            dfs(x2,ny2,0)

    # 현재 세로나 대각선이면, 아래로 밀 수 있음
    if d == 1 or d ==2:
        nx2 = x2 + 1
        if in_range(nx2, y2) and house[nx2][y2] != 1:
            dfs(nx2,y2,1)

    # 모두 대각선 이동 가능
    nx2 = x2 + 1
    ny2 = y2 + 1
    if in_range(nx2, ny2):
        if house[nx2][ny2] != 1 and house[nx2][ny2-1] != 1 and house[nx2-1][ny2] != 1:
            dfs(nx2,ny2,2)

dfs(0,1,0)
print(res)
