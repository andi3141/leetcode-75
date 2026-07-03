class Solution:
    def isValid(self, s: str) -> bool:
        n = len(s)
        if n % 2 != 0:
            return False

        o_to_c = {"(": ")", "[": "]", "{": "}"}
        queue = []
        
        for i in range(len(s)):
            if s[i] in ["(", "[", "{"]:
                queue.append(s[i])
                continue
            if len(queue) == 0:
                return False

            if o_to_c[queue[-1]] != s[i]:
                return False

            queue.pop(-1)

        if len(queue) > 0:
            return False

        return True
