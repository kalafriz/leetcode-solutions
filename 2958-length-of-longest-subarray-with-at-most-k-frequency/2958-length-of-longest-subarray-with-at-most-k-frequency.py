from collections import defaultdict
class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        
        # METHOD: sliding window
        # if subarray 'good' -> expand window to right
        # else -> shrink window from left until subarray is 'good' again
    
        result = 0
        current = 0
        
        n = len(nums)
        left, right = 0,0 # sliding window start/end
        freqDict = defaultdict(lambda: 0, {}) #init default freq to 0
        
        while right<n:
            x = nums[right]
            freqDict[x] +=1
            #print(x,freqDict[x], nums[left:right+1], current, result)
            
            while freqDict[x] > k: # remove leftmost elements from subarray until good
                freqDict[nums[left]] -=1
                current -=1
                left +=1
                #print(x,freqDict[x], nums[left:right+1], current, result)
            
            current+=1
            right+=1
            result = max(current, result)
        
        return result