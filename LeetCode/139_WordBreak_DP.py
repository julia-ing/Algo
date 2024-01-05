# 아래와 같은 재귀 방식은 시간복잡도가 2^n 이라서 시간 초과..
class Solution:
    def wordBreak(self, s, wordDict):
        def recurse(start):
            if start == len(s):
                return True
            for end in range(start + 1, len(s) + 1):
                if s[start:end] in wordDict and recurse(end):
                    return True
            return False

        return recurse(0)


# dp 방식, 솔루션 참고
class Solution2:
    def wordBreak(self, s, wordDict):
        dp = [False] * (len(s) + 1)
        dp[0] = True

        for i in range(1, len(s) + 1):
            for j in range(i):
                if s[j:i] in wordDict and dp[j]:
                    dp[i] = True
                    break
        return dp[len(s)]
