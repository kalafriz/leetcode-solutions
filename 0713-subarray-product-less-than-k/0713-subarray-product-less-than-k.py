import numpy as np
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k<=1:
            return 0
        
        # METHOD: sliding window
        # -> expand to next right element when prod < k
        # -> remove first leftmost element when prod >=k
        result = 0
        n = len(nums)
        prod = 1
        left, right = 0, 0
        
        while right < n:
            prod *= nums[right] # expand to next element on right
            
            while prod >= k: # remove leftmost element
                prod //= nums[left]
                left +=1
            
            result += right-left+1 # window size = # prod<k subarrays in window
            right +=1

        return result