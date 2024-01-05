class Solution:
    def lengthOfLongestSubstring(self, s):
        dp = [1] * len(s)
        char_idx_map = {}
        if s:
            char_idx_map[s[0]] = 0

        for i, char in enumerate(s[1:], start=1):
            if char not in char_idx_map:
                char_idx_map[char] = i
                dp[i] = dp[i - 1] + 1
            else:
                previous_idx = char_idx_map[char]
                dp[i] = min(i - previous_idx, dp[i - 1] + 1)
                char_idx_map[char] = i
        return max(dp) if dp else 0
