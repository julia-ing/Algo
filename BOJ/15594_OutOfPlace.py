N = int(input())
nums = [int(input()) for _ in range(N)]
sorted_nums = sorted(nums)

res = 0
for i in range(N):
    # 이미 정렬되어있으면 넘어감
    if nums[i] == sorted_nums[i]:
        continue
    # i부터 끝까지의 배열에서 정렬해야하는 위치를 찾고 swap
    for j in range(i, N):
        if sorted_nums[i] == nums[j] and sorted_nums[j] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
            res += 1
print(res)
