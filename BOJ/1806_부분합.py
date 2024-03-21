N, S = map(int, input().split())
nums = list(map(int, input().split()))

left, right = 0, 0
res = N+1
total = 0

while True:
    if total >= S:
        res = min(res, right - left)
        total -= nums[left]
        left += 1
    elif right == N:
        break
    else:
        total += nums[right]
        right += 1

if res == N+1:
    print(0)
else:
    print(res)