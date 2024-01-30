T, W = map(int, input().split())
drop = [0]
for _ in range(T):
    drop.append(int(input()))

dp = [[0] * (W+1) for _ in range(T+1)]

for i in range(1, T+1):
    # 움직이지 않을 경우 (첫줄) 초기화
    if drop[i] == 1:
        dp[i][0] = dp[i-1][0] + 1
    else:
        dp[i][0] = dp[i-1][0]
    
    for j in range(1, W+1):
        if j%2 == 0:
            curr = 1
        else:
            curr = 2
        
        # 만약 서있던 자리에서 자두가 떨어지면 + 1
        if drop[i] == curr:
            dp[i][j] = max(dp[i-1][j] + 1, dp[i-1][j-1] + 1)
        # 움직이는 경우 이전 값 그대로
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-1])

print(max(dp[T]))