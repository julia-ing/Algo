import heapq

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
conv = {}  # 편의점 (사람 : 좌표)
ppl = [[-1, -1] for _ in range(m)]  # 사람들 좌표
arrived = [0] * m  # 사람들의 도착 여부

for i in range(m):
    x, y = map(int, input().split())
    conv[i] = [x-1, y-1]

# 우선순위: 북서동남
dx = [-1, 0, 0, 1]
dy = [ 0, -1, 1, 0]

# 최단거리를 찾기 위한 다익스트라
# 타깃인 편의점 위치부터 시작!
def minDist(tx, ty, distance):
    q = []
    distance[tx][ty] = 0
    heapq.heappush(q, (tx, ty, 0))
    
    while q:
        x, y, dist = heapq.heappop(q)
        # 이미 방문한 경우
        if distance[x][y] < dist:
            continue
        # 다음 정점은 사방향 가능
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 범위 안에 있고 지날 수 잇는 경우에만
            if 0<=nx<n and 0<=ny<n and grid[nx][ny] != -1:
                if dist+1 < distance[nx][ny]:
                    distance[nx][ny] = dist+1
                    heapq.heappush(q, (nx, ny, dist+1))
                
def check():
    for i in range(m):
        if not arrived[i]:
            return False
    return True

res = 0
while True:
    res += 1

    for i in range(m):
        if arrived[i]:
            continue
        # 1,2 번은 격자 안에 있을 경우만
        if ppl[i] != [-1, -1]:
            # 1번: 편의점까지의 최단거리 찾아 1칸 이동
            distance = [[1e9]*n for _ in range(n)]
            minDist(conv[i][0], conv[i][1], distance)
            
            min_val = 1e9
            min_x, min_y = 0, 0
            for j in range(4):
                # 현재 사람의 위치에서 1칸 이동한 위치 ~ 편의점 거리 비교
                nx = ppl[i][0] + dx[j]
                ny = ppl[i][1] + dy[j]
                if 0<=nx<n and 0<=ny<n:
                    if min_val > distance[nx][ny]:
                        min_val = distance[nx][ny]
                        min_x, min_y = nx, ny
            ppl[i] = [min_x, min_y]

    # 2번: 도착했으면 멈추고, 지날 수 없다는 표시하기
    for i in range(m):
        if ppl[i] == conv[i]:
            arrived[i] = 1
            grid[ppl[i][0]][ppl[i][1]] = -1

    if res <= m:
        # 3번: 목표 편의점까지 최단거리의 베이스 캠프를 찾아 이동
        distance = [[1e9]*n for _ in range(n)]
        minDist(conv[res-1][0], conv[res-1][1], distance)
        min_val = 1e9
        min_x, min_y = 0, 0
        for i in range(n):
            for j in range(n):
                # 베이스 캠프들 ~ 편의점 거리 비교
                if grid[i][j] == 1:
                    if min_val > distance[i][j]:
                        min_val = distance[i][j]
                        min_x, min_y = i, j
        ppl[res-1] = [min_x, min_y]
        grid[min_x][min_y] = -1

    # 모든 사람이 도착하면 멈춤
    if check():
        break

print(res)
