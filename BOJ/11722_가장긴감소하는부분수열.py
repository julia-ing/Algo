n = int(input())
A = list(map(int, input().split()))

dp = [1] * n
# 10 30 10 20 20 10
# 1  1  2  2  2  3
for i in range(1, n):
    for j in range(i):
        if A[j] > A[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))
 