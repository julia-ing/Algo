# https://www.acmicpc.net/problem/3190
from collections import deque

n = int(input())
k = int(input())
board = [[0] * (n + 1) for _ in range(n + 1)]

for _ in range(k):
    a, b = map(int, input().split())
    board[a][b] = 1  # 사과가 있으면 1

l = int(input())
change = []
for _ in range(l):
    x, c = input().split()
    change.append((int(x), c))

# 동, 남, 서, 북
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def turn(direction, c):
    if c == "L":
        direction = (direction - 1) % 4
    else:
        direction = (direction + 1) % 4
    return direction


### 구현 ###
x, y = 1, 1
board[x][y] = 2  # 뱀이 있으면 2
direction = 0
time = 0
snake = deque()  # 뱀이 있는 위치 저장
snake.append((x, y))

while True:
    nx = x + dx[direction]
    ny = y + dy[direction]

    time += 1
    if 1 <= nx and nx <= n and 1 <= ny and ny <= n and board[nx][ny] != 2:
        # 사과 없음: 이동 후 꼬리 제거
        if board[nx][ny] == 0:
            board[nx][ny] = 2
            snake.append((nx, ny))
            px, py = snake.popleft()
            board[px][py] = 0
        # 사과 있음: 이동만
        else:
            board[nx][ny] = 2
            snake.append((nx, ny))
    else:
        break

    x, y = nx, ny

    if change and time == change[0][0]:
        direction = turn(direction, change[0][1])
        change.pop(0)

print(time)
