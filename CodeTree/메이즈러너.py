# 풀이 참고
# 정사각형 찾는 방법, 90도 회전하는 방법 익히자

import copy

N, M, K = map(int, input().split())
miro = [[0] * (N + 1) for _ in range(N + 1)]
for i in range(1, N+1):
    miro[i] = [0] + list(map(int, input().split()))

ppl = {}
for i in range(1, M+1):
    ppl[i] = list(map(int, input().split()))

ex, ey = map(int, input().split())
res = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dist(x1, y1, x2, y2):
    return abs(x1-x2) + abs(y1-y2)

def move(x, y, pi):
    global res
    cx, cy = x, y
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 1<=nx<N+1 and 1<=ny<N+1 and miro[nx][ny] == 0:
            if dist(nx, ny, ex, ey) < dist(x, y, ex, ey):
                cx, cy = nx, ny
                res += 1
                break
    ppl[pi] = [cx, cy]

def find_square():
    square = []
    for slen in range(2, N+1):
        for x1 in range(1, N-slen+2):  # 좌상단
            for y1 in range(1, N-slen+2):
                x2, y2 = x1+slen-1, y1+slen-1
                # 출구가 포함되어야 함
                if not (x1<=ex<=x2 and y1<=ey<=y2):
                    continue
                # 정사각형 안에 사람이 있는지 확인
                has_person = False
                for p in range(1, M+1):
                    px, py = ppl[p]
                    if x1<=px<=x2 and y1<=py<=y2:
                        # 출구에 있는 사람은 제외
                        if not (px==ex and py==ey):
                            has_person = True
                if has_person:
                    square = [x1, y1, slen]  # 좌상단 좌표와 정사각형의 길이
                    return square
    return square

def rotate():
    global miro, ppl, ex, ey
    # 한 명 이상의 참가자와 출구를 포함한 가장 작은 정사각형을 잡음
    sx, sy, slen = 0, 0, 0
    square = find_square()
    if square:
        sx, sy, slen = square
    # 회전된 벽은 내구도 -1
    for x in range(sx, sx+slen):
        for y in range(sy, sy+slen):
            if miro[x][y]:
                miro[x][y] -= 1
    ppl_check = [0] * (M+1)
    exit_check = 0
    # 판 회전
    temp = copy.deepcopy(miro)
    for x in range(sx, sx+slen):
        for y in range(sy, sy+slen):
            ox, oy = x-sx, y-sy  # 0, 0으로 옮겨놓고
            rx, ry = oy, slen-ox-1  # 회전 코드
            temp[rx+sx][ry+sy] = miro[x][y]  # 다시 +sx, +sy를 해줌
            # 사람 회전
            for p in ppl:
                if x == ppl[p][0] and y == ppl[p][1] and not ppl_check[p]:
                    ppl[p] = [rx+sx, ry+sy]
                    ppl_check[p] = 1  # 회전 완료 표시
            # 출구 회전
            if x == ex and y == ey and not exit_check:
                ex, ey = rx+sx, ry+sy
                exit_check = 1  # 회전 완료 표시
    miro = temp


for t in range(K):
    # 참가자 이동
    for p in ppl:
        move(ppl[p][0], ppl[p][1], p)
    # 출구로 나갔으면 없애기
    for p in ppl:
        if ppl[p][0] == ex and ppl[p][1] == ey:
            ppl[p] = [-1, -1]
    # 남은 사람 없으면 끝
    if not ppl:
        break
    # 회전
    rotate()

print(res)
print(ex, ey)