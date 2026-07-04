class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])

        nodesAttributed = set()
        numComponents = 0
        for i in range(m):
            for j in range(n):

                if (i,j) in nodesAttributed or grid[i][j] !='1':
                    continue

                nodesToCheck = {(i,j)}

                while len(nodesToCheck) > 0:
                    node = nodesToCheck.pop()
                    nodesAttributed.add(node)
                    
                    # land found
                    if grid[node[0]][node[1]] == "1": 
                        nn = self.getNeighbours(node[0], node[1], m, n)
                        nodesToCheck = nodesToCheck.union(nn.difference(nodesAttributed))
                
                numComponents +=1

        return numComponents

    def getNeighbours(self, i, j, m, n):
        nn = set()
        if i-1 >=0:
            nn.add((i-1, j))
        if i+1 < m:
            nn.add((i+1, j))
        if j-1 >=0:
            nn.add((i, j-1))
        if j+1 < n:
            nn.add((i, j+1))
        return nn