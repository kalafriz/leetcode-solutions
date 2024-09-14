class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        maxVal = 0
        currentArrLen, result = 0, 0
        
        for n in nums:
            
            # set new max val + reset subarray len
            if n > maxVal:
                maxVal = n
                currentArrLen, result = 0, 0
            
            # if max, continue or restart current subarray
            if n == maxVal:
                currentArrLen += 1
            
            # otherwise break current subarray
            else:
                currentArrLen = 0
            
            
            result = max(currentArrLen, result) # if we started a new subarr at same max and surpassed prev
            
        return result