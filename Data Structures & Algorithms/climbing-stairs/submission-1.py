class Solution:
    def climbStairs(self, n: int) -> int:
        
        if n ==1:
            return 1
        p = [0] * n
        p[0] = 1
        p[1] = 2
        for i in range(2, n, 1):
            p[i] = p[i-1] + p[i-2]
        # print(p)
        return p[n-1]
