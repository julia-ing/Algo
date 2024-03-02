from itertools import combinations

N, M = map(int, input().split())
nums = [i+1 for i in range(N)]

dist = [[1e9] * (N+1) for _ in range(N+1)]
for i in range(N+1):
    for j in range(N+1):
        if i==j:
            dist[i][j] = 0
            
for _ in range(M):
    a, b = map(int, input().split())
    dist[a][b] = 1
    dist[b][a] = 1

def floyd():
    for k in range(1, N+1):
        for i in range(1, N+1):
            for j in range(1, N+1):
                if (dist[i][k] + dist[k][j]) < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

floyd()
sum_val = 1e9
res = []
# 치킨집 두개 골라서 거리합 비교
for combi in combinations(nums, 2):
    temp = 0
    for i in range(1, N+1):
        temp += min(dist[combi[0]][i], dist[combi[1]][i])
    if temp < sum_val:
        sum_val = temp
        res = [combi[0], combi[1], sum_val*2]

print(*res)
