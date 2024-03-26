class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        smallest = 1
        nums.sort()
        
        for n in nums:
            if n==smallest:
                smallest +=1
        
        return smallest