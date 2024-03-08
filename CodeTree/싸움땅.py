n, m, k = map(int, input().split())

grid = []
for _ in range(n):
    row = list(map(int, input().split()))
    grid.append([[val] if val != 0 else [] for val in row])
players = {}

for i in range(m):
    x, y, d, s = map(int, input().split())
    players[i+1] = [x-1, y-1, d, s, 0]  # x, y, 방향, 능력치, 총 공격력

points = [0 for _ in range(m+1)]

# d: 위 오 아 왼
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def in_range(x, y):
    return 0<=x<n and 0<=y<n

def check_player(n, x, y):
    for p in players:
        if p != n:
            cx, cy = players[p][0], players[p][1]
            if x==cx and y==cy:
                return True, p
    return False, 0

def get_gun(p, guns):
    # 가장 공격력 높은 총을 획득하고 나머지 내려놓기
    if players[p][-1] != 0:
        guns.append(players[p][-1])
    guns.sort()
    # 가장 공격력 센 총을 획득
    players[p][-1] = guns[-1]
    grid[players[p][0]][players[p][1]] = guns[:-1]

def loser_move(p):
    px, py, d, s, a = players[p]
        
    for i in range(4):
        nd = (d+i) % 4
        nx = px + dx[nd]
        ny = py + dy[nd]
        is_player, other_num = check_player(p, nx, ny)
        # 다른 플레이어가 있거나 범위 밖이면 오른쪽으로 회전하며 빈 칸이 보이는 순간 이동
        if not is_player and in_range(nx, ny):
            players[p] = [nx, ny, nd, s, 0]
            # 만약 총이 있다면
            if grid[nx][ny]:
                # 가장 공격력 높은 총을 획득하고 나머지 내려놓기
                get_gun(p, grid[nx][ny])
            break

def fight(p1, p2, x, y):
    p1_s, p1_a = players[p1][3], players[p1][4]
    p2_s, p2_a = players[p2][3], players[p2][4]
    if p1_s + p1_a < p2_s + p2_a:
        winner = p2
    elif p1_s + p1_a > p2_s + p2_a:
        winner = p1
    else:
        if p1_s < p2_s:
            winner = p2
        else:
            winner = p1
    # 이긴 플레이어는 초기 능력치와 총의 공격력의 합의 차이만큼을 포인트로 획득
    if winner == p1:
        points[p1] += (p1_s + p1_a) - (p2_s + p2_a)
        # 진 플레이어는 총을 격자에 내려놓고
        if p2_a > 0:
            grid[x][y].append(p2_a)
        loser_move(p2)  # 이동
        # 이긴 플레이어 총 갈아끼우기
        if grid[players[p1][0]][players[p1][1]]:
            get_gun(p1, grid[players[p1][0]][players[p1][1]])
    else:
        points[p2] += (p2_s + p2_a) - (p1_s + p1_a)
        # 진 플레이어는 총을 격자에 내려놓고
        if p1_a > 0:
            grid[x][y].append(p1_a)
        loser_move(p1)  # 이동
        # 이긴 플레이어 총 갈아끼우기
        if grid[players[p2][0]][players[p2][1]]:
            get_gun(p2, grid[players[p2][0]][players[p2][1]])

def action():
    for p in players:
        # 이동
        x, y, d, s, a = players[p]
        nx = x + dx[d]
        ny = y + dy[d]
        # 격자를 벗어나는 경우
        if not in_range(nx, ny):
            # 방향을 정반대로 바꾸기
            d = (d+2)%4
            nx = x + dx[d]
            ny = y + dy[d]
        # 1칸 이동
        players[p] = [nx, ny, d, s, a]

        # --2번--
        is_player, other_num = check_player(p, nx, ny)
        # 플레이어가 없다면 총이 있는지 확인
        if not is_player:
            guns = grid[nx][ny]
            if guns: # 총이 있으면
                get_gun(p, guns)
        # 플레이어가 있다면 두 플레이어가 싸움
        else:
            fight(p, other_num, nx, ny)

for _ in range(k):
    action()

print(*points[1:])
