x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())

# cow feed 가 세로를 모두 가리는 경우
if y4 > y2 and y1 > y3:
    if x3 < x2 < x4:
        x2 = x3
    if x3 < x1 < x4:
        x1 = x4
# cow feed 가 가로를 모두 가리는 경우
if x4 > x2 and x1 > x3:
    if y3 < y2 < y4:
        y2 = y3
    if y3 < y1 < y4:
        y1 = y4

print((x2-x1) * (y2-y1))