n = int(input())
score = []
for _ in range(n):
    num = int(input())
    score.append(num)

# 10 20 15 25 10 20
# 10 30 35 55 65 75
# max(이전 score + 그 전전 dp , 전전 dp) + 현재 score
if n <= 2:
    print(sum(score))
    exit(0)

dp = [0] * n
dp[0] = score[0]
dp[1] = score[0] + score[1]
dp[2] = max(score[0] + score[2], score[1] + score[2])
for i in range(3, n):
    dp[i] = max(score[i-1] + dp[i-3], dp[i-2]) + score[i]

print(dp[-1])