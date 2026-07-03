import numpy as np


class Solution:
    def longestPalindrome(self, s: str) -> str:
        # DP
        n = len(s)
        dp = np.zeros([len(s), len(s)], bool)
        maxL = 0
        maxP = ""
        for j in range(n):
            for i in range(n):
                if i > j:
                    continue
                if np.absolute(i - j) <= 2:
                    dp[i, j] = True if s[i] == s[j] else False
                else:
                    dp[i, j] = dp[i + 1, j - 1] if s[i] == s[j] else False
                # update max len and max palindrome
                if dp[i, j] and j - i + 1> maxL:
                    maxL = j - i
                    maxP = s[i : j + 1]

        return maxP
