lx1, ly1, rx1, ry1 = map(int, input().split())
lx2, ly2, rx2, ry2 = map(int, input().split())
t_lx, t_ly, t_rx, t_ry = map(int, input().split())

# block 된 면적의 가로 세로 길이를 구하기 위한 함수
# 오른쪽 상단 값 중 min - 왼쪽 하단 값 중 max
def calc_blocked(t1, b1, t2, b2):
    return max(0, min(t1, b1) - max(t2, b2))

blocked_1 = calc_blocked(t_rx, rx1, t_lx, lx1) * calc_blocked(t_ry, ry1, t_ly, ly1)
blocked_2 = calc_blocked(t_rx, rx2, t_lx, lx2) * calc_blocked(t_ry, ry2, t_ly, ly2)
total = (rx1-lx1) * (ry1-ly1) + (rx2-lx2) * (ry2-ly2)

print(total - blocked_1 - blocked_2)
