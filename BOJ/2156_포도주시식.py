n = int(input())
podo = []
for _ in range(n):
    podo.append(int(input()))
if n == 1:
    print(podo[0])
    exit(0)

dp = [0] * n
dp[0] = podo[0]
dp[1] = podo[0] + podo[1]

# 6 10 13 9 8 1
# 6 16 19 28 

# 100 100 0 0 100 100
# 100 200 200 200 300 400

for i in range(2, n):
    dp[i] = max(dp[i-1], dp[i-2] + podo[i], dp[i-3] + podo[i-1] + podo[i])
print(max(dp))
