from collections import deque
from pprint import pprint

N = int(input())
board = [[0] * N for _ in range(N)]
K = int(input()) # 사과 개수

for _ in range(K):
    x, y = map(int, input().split())
    board[x-1][y-1] = 2 # 사과

# pprint(board)

# 오른쪽부터 시계 방향 (동남서북)
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

# 'L': 왼쪽, 'D': 오른쪽으로 90도
def turn(c):
    global direction
    if c == 'L':
        direction = (direction-1) % 4
    else:
        direction = (direction+1) % 4


XC = {}  # 방향 변환 저장
L = int(input()) # 방향 변환 횟수
for _ in range(L):
    x, c = input().split()
    XC[int(x)] = c

q = deque() # 뱀 위치 저장
q.append((0, 0))
x, y = 0, 0
board[x][y] = 1 # 뱀

direction = 0
time = 0

while q:
    pprint(board)
    time += 1
    # 다음 칸에 위치할 머리
    nx = x + dx[direction]
    ny = y + dy[direction]

    # 벽이나 몸에 부딪히면 끝
    if 0 > nx or nx >= N or 0 > ny or ny >= N or board[nx][ny] == 1:
        break

    # 사과가 없으면
    elif board[nx][ny] == 0:
        # 꼬리 비워주기
        tx, ty = q.popleft()
        board[tx][ty] = 0

    # 사과가 있든 없든 머리는 늘어남
    board[nx][ny] = 1
    q.append((nx, ny))

    # 다음 시작점 갱신
    x, y = nx, ny

    # 회전
    if time in XC:
        turn(XC[time])

print(time)
