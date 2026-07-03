class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxLen = 1
        p = s[0]
        for i in range(len(s) - 1):
            s1 = self.checkForUnevenPalindrome(s, i)
            if len(s1) > maxLen:
                maxLen = len(s1)
                p = s1
            s2 = self.checkForEvenPalindrome(s, i)
            if len(s2) > maxLen:
                maxLen = len(s2)
                p = s2
        return p

    def checkForEvenPalindrome(self, s, i):
        print(i)
        if i + 1 >= len(s) or s[i] != s[i + 1]:
            return ""

        k = 0
        while i - k >= 0 and i + k + 1 < len(s) and s[i - k] == s[i + k + 1]:
            k += 1
        k -= 1
        return s[i - k : i + k + 2]

    def checkForUnevenPalindrome(self, s, i: int) -> str:
        if len(s) == 1:
            return s

        k = 1
        while i - k >= 0 and i + k <= len(s) - 1 and s[i - k] == s[i + k]:
            k += 1
        return s[i - k + 1 : i + k]
