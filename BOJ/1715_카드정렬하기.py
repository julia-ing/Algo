import heapq

N = int(input())
nums = []
for _ in range(N):
    heapq.heappush(nums, int(input()))

res = 0
while len(nums) >= 2:
    a = heapq.heappop(nums)
    b = heapq.heappop(nums)
    
    sum_val = a+b
    res += sum_val
    heapq.heappush(nums, sum_val)

print(res)