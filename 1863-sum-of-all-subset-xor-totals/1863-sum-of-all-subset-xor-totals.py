class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        result = 0
        
        for x in nums:
            result |= x
            
            
        return result << (len(nums)-1)