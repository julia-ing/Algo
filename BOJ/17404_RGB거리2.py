N = int(input())
house = [[0, 0, 0]]
INF = 1e9

for i in range(N):
    house.append(list(map(int, input().split())))

ans = INF
for i in range(3):
    dp = [[0]*3 for _ in range(N+1)]
    dp[1] = [INF, INF, INF]
    # 1번 고정
    dp[1][i] = house[1][i]
    
    for j in range(2, N+1):
        dp[j][0] = min(dp[j-1][1], dp[j-1][2]) + house[j][0]
        dp[j][1] = min(dp[j-1][0], dp[j-1][2]) + house[j][1]
        dp[j][2] = min(dp[j-1][0], dp[j-1][1]) + house[j][2]

    # 1번과 N번의 색이 달라야 함
    dp[N][i] = INF
    ans = min(ans, min(dp[N]))

print(ans)
