N = int(input())
covered = [0] * 1000 # 라이프가드 수
time = []
for _ in range(N):
    start, end = map(int, input().split())
    time.append((start, end))
    for i in range(start, end):
        covered[i] += 1

# lifeguard 로 커버되는 수
total = 0
for cov in covered:
    if cov > 0:
        total += 1

# 커버되지 않는 수 하나씩 계산: start~end 까지 1 이하면 하나를 뺐을 때 커버를 못하는 곳
min_not_cov = 1e9
for s, e in time:
    temp = 0
    for i in range(s, e):
        if covered[i] <= 1:
            temp += 1
    min_not_cov = min(temp, min_not_cov)

print(total - min_not_cov)
