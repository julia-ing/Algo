class Solution:
    def longestConsecutive(self, nums):
        if not nums:
            return 0
        sort = sorted(nums)
        n = len(sort)
        dp = [0] * n
        for i in range(1, n):
            if sort[i] == sort[i-1] + 1:
                dp[i] = dp[i-1] + 1
            elif sort[i] == sort[i-1]:
                dp[i] = dp[i-1]

        return max(dp) + 1
