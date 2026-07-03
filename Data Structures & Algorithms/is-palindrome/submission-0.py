
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r'[^a-zA-Z0-9]', '', s)
        s = s.lower()
        print(s)
        n = len(s)
        h = math.floor(len(s) / 2)
        for i in range(h):
            if s[i] != s[n - i - 1]:
                return False
        return True
