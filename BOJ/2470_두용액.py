N = int(input())
nums = list(map(int, input().split()))
nums.sort()

l = 0
r = N-1

res = abs(nums[l] + nums[r])
value = [nums[l], nums[r]]

while l < r:
    left = nums[l]
    right = nums[r]
    
    sum_lr = left + right
    if abs(sum_lr) < res:
        res = abs(sum_lr)
        value = [left, right]
        if res == 0:
            break
        
    if sum_lr < 0:
        l += 1
    else:
        r -= 1

print(value[0], value[1])
