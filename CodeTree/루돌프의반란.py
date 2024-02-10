N, M, P, C, D = map(int, input().split())
rx, ry = map(int, input().split())

santa = {}
score = [0] * (P+1)  # 산타 점수
faint = [0] * (P+1)  # 기절 상태

for _ in range(P):
    si, sx ,sy = map(int, input().split())
    santa[si] = [sx, sy]

def in_range(x, y):
    return 1<=x<N+1 and 1<=y<N+1


def interaction(si, dx ,dy):
    new_x = santa[si][0] + dx
    new_y = santa[si][1] + dy
    if not in_range(new_x, new_y):
        del santa[si]
        faint[si] = 0
    else:
        # 다른 산타가 있으면 상호작용
        for other_santa in santa.copy().keys():
            if other_santa == si:
                continue
            if santa.get(other_santa) and santa[other_santa][0] == new_x and santa[other_santa][1] == new_y:
                interaction(other_santa, dx, dy)
        santa[si] = [new_x, new_y]


# 충돌, type: 루돌프가 움직여 충돌난건지(0), 산타가 움직여 충돌난건지(1)
def collision(type, x, y, dx, dy, si):
    if type == 0:
        plus = C
    else:
        plus = D
    
    score[si] += plus
    
    # 루돌프가 이동해온 방향 or 산타가 이동해온 반대방향으로 plus 만큼 이동
    x += dx*plus
    y += dy*plus
    
    # 게임판 밖이라면 탈락
    if not in_range(x, y):
        del santa[si]
        faint[si] = 0
    else:
        # 기절, 다른 산타가 있으면 상호작용
        if type == 0:
            faint[si] = 2
        else:
            faint[si] = 1
        for other_santa in santa.copy().keys():
            if other_santa == si:
                continue
            if santa.get(other_santa) and santa[other_santa][0] == x and santa[other_santa][1] == y:
                interaction(other_santa, dx, dy)
        santa[si] = [x, y]


def r_move():
    global rx, ry
    # 가장 가까운 산타 찾아 1칸 돌진
    now = 1e9
    cx, cy, ci = rx, ry, 0
    for si in santa:
        sx, sy = santa[si]
        dist = (rx-sx)**2 + (ry-sy)**2
        if dist < now:
            cx, cy, ci = sx, sy, si
            now = dist
        elif dist == now:
            if sx > cx:
                cx, cy, ci = sx, sy, si
                now = dist
            elif sx == cx:
                if sy > cy:
                    cx, cy, ci = sx, sy, si
                    now = dist
    # 가장 가까운 산타에게 가는 방향 구하기
    move_x, move_y = 0, 0
    if cx > rx:
        move_x = 1
    elif cx < rx:
        move_x = -1
    if cy > ry:
        move_y = 1
    elif cy < ry:
        move_y = -1
    # 돌진
    rx += move_x
    ry += move_y
    
    # 만약 루돌프의 움직임으로 산타와 충돌하는 경우
    if rx == cx and ry == cy:
        collision(0, cx, cy, move_x, move_y, ci)

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def s_move():
    for i in range(1, P+1):
        # 기절하면 움직일 수 없음
        if faint[i] > 0:
            faint[i] -= 1
            continue
        # 탈락한 산타는 제외하고 움직임
        if santa.get(i):
            # 루돌프에게 가장 가까워지는 방향 찾기
            sx, sy = santa[i][0], santa[i][1]
            now = (rx-sx)**2 + (ry-sy)**2
            move_x, move_y = 0, 0
            cand = []
            for d in range(4):
                nx = sx + dx[d]
                ny = sy + dy[d]
                dist = (rx-nx)**2 + (ry-ny)**2
                if dist < now:
                    # 다른 산타가 있으면 움직이지 않음
                    is_santa = False
                    for s in santa:
                        if s == i:
                            continue
                        if santa[s][0] == nx and santa[s][1] == ny:
                            is_santa = True
                            break
                    if not is_santa and in_range(nx, ny):
                        cand.append((nx, ny, dist, d))
            if not cand:
                continue
            else:
                # 우선순위: 거리 -> 방향
                cand.sort(key=lambda x: (x[2], x[3]))
                cx, cy, _, cd = cand[0]
                # 루돌프와 충돌 or 바로 이동
                if cx == rx and cy == ry:
                    collision(1, cx, cy, dx[(cd+2)%4], dy[(cd+2)%4], i)
                else:
                    santa[i] = [cx, cy]
            

for t in range(M):
    # 루돌프 움직임
    r_move()
    # 산타 움직임
    s_move()
    # 살아남은 산타들 +1점
    for s in santa:
        score[s] += 1

print(*score[1:])
