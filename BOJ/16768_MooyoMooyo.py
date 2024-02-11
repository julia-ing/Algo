from collections import deque
from pprint import pprint

N, K = map(int, input().split())
board = [list(map(int, list(input()))) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def find_connected_region(i, j):
    q = deque()
    q.append((i, j))
    visited[i][j] = 1
    connected = [(i, j)]
    
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<N and 0<=ny<10 and not visited[nx][ny] and board[nx][ny] == board[x][y]:
                visited[nx][ny] = 1
                connected.append((nx, ny))
                q.append((nx, ny))
    return connected


def gravity(board):
    for c in range(10):
        # 맨 아랫줄부터 역순으로 탐색
        drop = N - 1  # 숫자를 내릴 위치, 마지막 행부터 시작
        for r in range(N-1, -1, -1):
            if board[r][c] != 0:
                while drop > r:
                    if board[drop][c] == 0:
                        board[drop][c], board[r][c] = board[r][c], board[drop][c]
                        break
                    drop -= 1  # 한 칸 위로 이동
    return board


while True:
    to_zero = []
    visited = [[0]*10 for _ in range(N)]
    for i in range(N):
        for j in range(10):
            if board[i][j] != 0 and not visited[i][j]:
                connected = find_connected_region(i, j)
                # K 이상인 지역들
                if len(connected) >= K:
                    to_zero += connected
    if not to_zero:
        break

    # 0으로 바꾸기
    for x, y in to_zero:
        board[x][y] = 0

    pprint(board)
    # gravity 처리
    gravity(board)
    pprint(board)

for row in range(N):
    print("".join([str(x) for x in board[row]]))
