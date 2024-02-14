from collections import deque

N, M, K = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

# 가장 최근에 공격한 포탑이 어느 위치인지 알기 위해 공격 업데이트
att = [[0] * (M) for _ in range(N)]

def elect_attacker(t):
    # 부서지지 않은 포탑 중 가장 약한 포탑
    candidate = []
    for i in range(N):
        for j in range(M):
            if grid[i][j] > 0:
                candidate.append((grid[i][j], i, j, att[i][j]))
    
    candidate.sort(key=lambda x: (-x[0], x[3], x[1]+x[2], x[2]))
    # 핸디캡 적용
    att_x, att_y = candidate[-1][1], candidate[-1][2]
    grid[att_x][att_y] += N+M
    victim_x, victim_y = candidate[0][1], candidate[0][2]
    att[att_x][att_y] = t
    return att_x, att_y, victim_x, victim_y

# 우/하/좌/상
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def attack(att_x, att_y, victim_x, victim_y):
    # 레이저 공격이 가능한지 확인
    visited = [[0] * (M) for _ in range(N)]
    q = deque()
    q.append((att_x, att_y))
    visited[att_x][att_y] = 1
    prev = {} # 이전 좌표 저장
        
    possible = False
    path = []
    
    while q:
        x, y = q.popleft()
        if x == victim_x and y == victim_y:
            while (x, y) != (att_x, att_y):
                path.append((x, y))
                x, y = prev[(x, y)]
            path.append((att_x, att_y))
            possible = True
            break
        for i in range(4):
            nx = (x + dx[i]) % N
            ny = (y + dy[i]) % M
            
            # 부서진 포탑은 지나갈 수 없음
            if grid[nx][ny] <= 0 or visited[nx][ny]:
                continue
            visited[nx][ny] = 1
            prev[(nx, ny)] = (x, y)
            q.append((nx, ny))

    if possible:
        # 레이저 공격
        for i in range(N):
            for j in range(M):
                if (i, j) in path:
                    if (i, j) == (att_x, att_y):
                        continue
                    elif (i, j) == (victim_x, victim_y):
                        grid[i][j] -= grid[att_x][att_y]
                    else:
                        grid[i][j] -= grid[att_x][att_y] // 2
                else:
                    if grid[i][j] > 0:
                        grid[i][j] += 1
    else:
        # 포탄 공격
        victims = []
        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                nx = (victim_x + i) % N
                ny = (victim_y + j) % M
                if grid[nx][ny] <= 0:
                    continue
                victims.append((nx, ny))
                
                
        for i in range(N):
            for j in range(M):
                if (i, j) == (att_x, att_y):
                    continue
                elif (i, j) == (victim_x, victim_y):
                    grid[i][j] -= grid[att_x][att_y]
                elif (i, j) in victims:
                    grid[i][j] -= grid[att_x][att_y] // 2
                else:
                    if grid[i][j] > 0:
                        grid[i][j] += 1

for t in range(K):
    # 남아있는 포탑
    alive = 0
    for i in range(N):
        for j in range(M):
            if grid[i][j] > 0:
                alive += 1
    
    if alive <= 1:
        break
                
    # 공격자와 공격 대상 선정
    att_x, att_y, victim_x, victim_y = elect_attacker(t+1)
    # 공격
    attack(att_x, att_y, victim_x, victim_y)
    
    for i in range(N):
        for j in range(M):
            if grid[i][j] < 0:
                grid[i][j] = 0


res = 0
for i in range(N):
    for j in range(M):
        res = max(res, grid[i][j])
print(res)
