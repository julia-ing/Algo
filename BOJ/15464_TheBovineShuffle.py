N = int(input())
order = list(map(int, input().split()))
cows = list(map(int, input().split()))

res = [0] * N
for j in range(3):
    for i in range(N):
        res[i] = cows[order[i]-1]
    cows = res.copy()

print(*res)
