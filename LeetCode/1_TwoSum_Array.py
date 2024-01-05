# 1. brute force
class Solution:
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]


# 2. for -> in
class Solution2:
    def twoSum(self, nums, target):
        for i, num in enumerate(nums):
            second = target - num
            if second in nums[i+1:]:
                return [i, nums[i+1:].index(second) + i + 1]


# 3. hashMap
class Solution3:
    def twoSum(self, nums, target):
        hashTable = {}
        for i in range(len(nums)):
            second = target - nums[i]
            if second in hashTable:  # 나머지 값이 맵에 있으면
                return sorted([i, hashTable[second]])  # 저장된 인덱스를 불러옴
            hashTable[nums[i]] = i  # 숫자와 인덱스를 맵에 저장
