import numpy as np
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        self.m = len(heights)
        self.n = len(heights[0])
        self.heights = np.array(heights)
        # pacific
        nodes1 = self.getReachableNodes((np.inf, 0))
        # atlantic
        nodes2 = self.getReachableNodes((0, np.inf))
        nodes = nodes1.intersection(nodes2)
        return [[n[0], n[1]] for n in nodes]
    def getReachableNodes(self, start):
        unvisisted = self.getNeighbours(start[0], start[1])
        reachable = set()
        while len(unvisisted) > 0:
            node = unvisisted.pop()
            reachable.add(node)
            neighbours = self.getNeighbours(node[0], node[1])
            unvisisted = unvisisted.union(neighbours).difference(reachable)
        return reachable

    def getNeighbours(self, i, j):
        nn = set()
        m = self.m
        n = self.n
        heights = self.heights

        # pacific
        if i == np.inf:
            for k in range(m):
                nn.add((k, 0))
            for k in range(n):
                nn.add((0, k))
            return nn
        # atlantic
        if j == np.inf:
            for k in range(m):
                nn.add((k, n-1))
            for k in range(n):
                nn.add((m-1, k))
            return nn

        if i-1 >= 0:
            if heights[i-1, j] >= heights[i, j]:
                nn.add((i-1, j))

        if i+1 < m:
            if heights[i+1, j] >= heights[i, j]:
                nn.add((i+1, j))
        if j-1 >= 0:
            if heights[i, j-1] >= heights[i, j]:
                nn.add((i, j-1))
        if j+1 < n:
            if heights[i, j + 1] >= heights[i, j]:
                nn.add((i, j+1))
        return nn