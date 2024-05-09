class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        
        happiness.sort()
        
        result = 0
        i = 0
        while i < k:
            child = happiness[-(i+1)] - i
            result += child if child > 0 else 0
            i+=1
            
        return result