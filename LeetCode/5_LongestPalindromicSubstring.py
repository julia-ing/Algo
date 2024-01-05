# first try: time exceeded..
class Solution:
    def isPalindrome(self, s):
        return s == s[::-1]

    def longestPalindrome(self, s: str) -> str:
        max_palindrome = ""
        for i in range(len(s)+1):
            for j in range(i):
                target = s[j:i]
                if self.isPalindrome(target):
                    if len(max_palindrome) < len(target):
                        max_palindrome = target
        return max_palindrome


# second
class Solution2:
    def isPalindrome(self, s):
        return s == s[::-1]

    def longestPalindrome(self, s: str) -> str:
        for i in range(len(s)):
            for j in range(i+1):
                if self.isPalindrome(s[j:len(s) - i + j]):  # 긴 부분 문자열부터 체크; max 를 리턴하기 위함
                    return s[j:len(s) - i + j]
