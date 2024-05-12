class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        
        n = len(grid)
        result = [[0 for i in range(n-2)] for j in range(n-2)]
        
        for i in range(1, n-1):
            for j in range(1, n-1):
                result[i-1][j-1] = max(max(grid[i-1][j-1:j+2]),max(grid[i][j-1:j+2]),max(grid[i+1][j-1:j+2]))
                
        return result