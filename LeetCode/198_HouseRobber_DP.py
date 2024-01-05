class Solution:
    def rob(self, nums):
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])

        dp = [0] * n
        dp[0], dp[1], dp[2] = nums[0], nums[1], nums[2] + nums[0]

        for i in range(3, n):
            dp[i] = nums[i] + max(dp[i - 2], dp[i - 3])

        return max(dp[-1], dp[-2])
