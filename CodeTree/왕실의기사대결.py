from collections import deque

L, N, Q = map(int, input().split())
# 1 = 함정, 2 = 벽
chess = [list(map(int, input().split())) for _ in range(L)]

# 기사 위치
knight = {}
# 초기 기사 체력, 업데이트할 기사 체력
initial_k_map, k_map = {}, {}
# 기사 맵
knight_map = [[0]*L for _ in range(L)]
for i in range(1, N+1):
    # 기사
    r, c, h, w, k = map(int, input().split())
    knight[i] = []
    for x in range(r, r+h):
        for y in range(c, c+w):
            knight[i].append((x-1, y-1))
            knight_map[x-1][y-1] = i
    initial_k_map[i] = k
    k_map[i] = k

# 방향 위,오,아,왼
direction = [(-1,0), (0,1), (1,0), (0,-1)]


def move(i,d):
    global knight, knight_map
    new_knight_map = [[0]*L for _ in range(L)]
    q = deque()
    q.append(i)
    need_move = set()
    while q:
        n = q.popleft()
        need_move.add(n)
        # tmp = set()
        for x, y in knight[n]:
            nx, ny = x + direction[d][0], y + direction[d][1]
            # 벽이 있으면 리턴
            if not (0<=nx<L and 0<=ny<L) or chess[nx][ny] == 2:
                return []
            # 내가 아닌 다른 기사가 있으면 그 기사도 이동
            if knight_map[nx][ny] != n and knight_map[nx][ny] > 0:
                q.append(knight_map[nx][ny])
    # 이동
    for n in need_move:
        a = []
        for x, y in knight[n]:
            nx, ny = x + direction[d][0], y + direction[d][1]
            new_knight_map[nx][ny] = n
            a.append((nx,ny))
        knight[n] = a

    # 이동하지 않는 기사
    for n in knight:
        if n not in need_move:
            for x, y in knight[n]:
                new_knight_map[x][y] = n

    knight_map = new_knight_map
    return need_move


# 대결
def fight(n, need_move):
    global res
    # 이동한 기사들에 대해, 함정이 있으면 대미지
    for i in need_move:
        for x, y in knight[i]:
            if i != n and chess[x][y] == 1:
                k_map[i] -= 1

# 명령
for q in range(Q):
    i, d = map(int, input().split())
    # 존재하는 기사에 대해서만
    if i in knight:
        # 벽이 없는 경우 확인하고 이동
        need_move = move(i, d)
        fight(i, need_move)
        # 대미지가 체력 이상이면 사라짐
        for n in range(1, len(k_map)+1):
            if n in k_map and k_map[n] <= 0:
                knight.pop(n)
                k_map.pop(n)
                for x in range(L):
                    for y in range(L):
                        if knight_map[x][y] == n:
                            knight_map[x][y] = 0

# 생존한 기사들 대미지 계산
res = 0
for i in range(1, len(initial_k_map) + 1):
    if i in k_map:
        res += initial_k_map[i] - k_map[i]
print(res)
