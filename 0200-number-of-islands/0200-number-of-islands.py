class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        num_islands = 0
        rows, cols = len(grid), len(grid[0])
        
        def dfs(i, j):
            # Finding an island will DFS for the rest of it, 
            # so we mark them as visited with '0' so we don't count it in a different islands DFS
            if i<0 or i>=rows or j<0 or j>=cols or grid[i][j]=="0":
                return
            else:
                grid[i][j]="0"
                dfs(i+1, j)
                dfs(i-1, j)
                dfs(i, j+1)
                dfs(i, j-1)
        
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    num_islands +=1
                    dfs(r,c)
        
        return num_islands