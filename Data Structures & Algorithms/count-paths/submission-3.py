import numpy as np


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid = np.zeros([m, n], int)
        grid[:, 0] = 1
        grid[0, :] = 1
        for i in range(1, m):
            for j in range(1, n):
                grid[i, j] = grid[i - 1, j] + grid[i, j - 1]
        return int(grid[m-1, n-1])
