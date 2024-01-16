from itertools import combinations
N, M = map(int, input().split())

city = [list(map(int, input().split())) for _ in range(N)]


def calculate_min_chicken(x, y, chicken):
    res = 1e9
    for i, j in chicken:
        temp = abs(x-i) + abs(y-j)
        if temp < res:
            res = temp
    return res

# 치킨 집 정보
chicken = []
for i in range(N):
    for j in range(N):
        if city[i][j] == 2:
            chicken.append((i, j))

ans = 1e9
# 치킨집 고르기
for chi in list(combinations(chicken, M)):
    # 치킨 거리
    res = 0
    for i in range(N):
        for j in range(N):
            if city[i][j] == 1:
                res += calculate_min_chicken(i, j, chi)
    if res < ans:
        ans = res
print(ans)