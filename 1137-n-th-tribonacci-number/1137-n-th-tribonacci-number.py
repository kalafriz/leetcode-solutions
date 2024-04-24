class Solution:
    def tribonacci(self, n: int) -> int:
        if n==0:
            return 0
        if n==1 or n==2:
            return 1
        
        tribs = [0] * (n+1)
        tribs[1], tribs[2] = 1, 1
        
        for i in range(3, n+1):
            tribs[i] = tribs[i-1]+tribs[i-2]+tribs[i-3]
            
        return tribs[n]
        