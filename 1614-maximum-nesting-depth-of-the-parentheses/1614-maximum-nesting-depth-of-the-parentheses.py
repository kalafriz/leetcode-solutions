class Solution:
    def maxDepth(self, s: str) -> int:
        
        maxDepth, currentDepth = 0,0
        
        for c in s:
            if c == '(':
                currentDepth +=1
                maxDepth = max(currentDepth, maxDepth)
            if c==')':
                currentDepth -=1
        
        return maxDepth;