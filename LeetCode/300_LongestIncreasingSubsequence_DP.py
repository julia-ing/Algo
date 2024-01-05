from bisect import bisect_left


# 1. common dynamic programming
class Solution1:
    def lengthOfLIS(self, nums):
        dp = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)


# 2. binary search
class Solution2:
    def lengthOfLIS(self, nums):
        tmp = [nums[0]]
        for x in nums[1:]:
            if tmp[-1] < x:  # x가 리스트 마지막 요소보다 크면
                tmp.append(x)
            else:
                idx = bisect_left(tmp, x)  # x를 삽입할 위치를 찾아 해당 위치의 값을 갈아 끼운다
                tmp[idx] = x
        return len(tmp)
