import heapq

n = int(input())
maze = [list(map(int, input())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

q = []
heapq.heappush(q, (0, 0, 0)) # x, y, 바꿔야하는 타일 수
flip = [[1e9]*n for _ in range(n)]
flip[0][0] = 0 # 시작

# 1: 흰, 0: 검
while True:
    x, y, t = heapq.heappop(q)
    # 끝에 도달하면 끝
    if x == n-1 and y == n-1:
        print(t)
        break
    for i in range(4):
        # 모든 방향 탐색
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<n and 0<=ny<n:
            # 이미 방문했다면 넘어감
            if flip[nx][ny] != 1e9:
                continue
            if maze[nx][ny] == 1:
                # 흰색이면 flip 갱신후 그대로 push
                if flip[nx][ny] > t: 
                    flip[nx][ny] = t    
                    heapq.heappush(q, (nx, ny, t))
            else:
                # 검은색이면 뒤집어야 함
                if flip[nx][ny] > t + 1:
                    flip[nx][ny] = t + 1
                    heapq.heappush(q, (nx, ny, t+1))
