import sys
sys.setrecursionlimit(10 ** 8)

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def dfs(x, y):
    if x<0 or x>=n or y<0 or y>=m or board[x][y] != 0:
        return
    board[x][y] = -1
    for i in range(4):
        dfs(x+dx[i], y+dy[i])

def canMelt(x, y):
    cnt = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<n and 0<=ny<m and board[nx][ny] == -1:
            cnt += 1
    return cnt >= 2

def findCheeseToMelt():
    cheese = []
    for x in range(n):
        for y in range(m):
            if canMelt(x, y) and board[x][y] == 1:
                cheese.append([x, y])
    return cheese


def solution():
    res = 0
    dfs(0, 0)
    while True:
        cheese = findCheeseToMelt()
        if not cheese:
            break
        for x, y in cheese:
            board[x][y] = 0
            dfs(x, y)
        res += 1
    return res

answer = solution()
print(answer)
