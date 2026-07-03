class Solution:
    def climbStairs(self, n: int) -> int:
        
        if n == 2:
            return 2
        p2 = 1
        p1 = 2
        p = 1
        for i in range(2, n, 1):
            print(p1, p2, p)
            p = p1 + p2
            p2 = p1
            p1 = p
        return p
