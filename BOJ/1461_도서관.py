N, M = map(int, input().split())
nums = list(map(int, input().split()))
# 양수 음수 나누기
positive = []
negative = []
max_walk = 0
for num in nums:
    if num < 0:
        negative.append(num)
    elif num > 0:
        positive.append(num)
    if abs(max_walk) < abs(num):
        max_walk = num
        
positive.sort(reverse=True)
negative.sort()

ans = abs(max_walk)
for i in range(0, len(negative), M):
    if negative[i] != max_walk:
        ans += 2*abs(negative[i])
for i in range(0, len(positive), M):
    if positive[i] != max_walk:
        ans += 2*abs(positive[i])
print(ans)