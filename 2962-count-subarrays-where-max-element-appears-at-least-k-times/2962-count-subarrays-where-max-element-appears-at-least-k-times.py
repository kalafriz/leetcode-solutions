class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        
        # METHOD: sliding window
        # let m = max(nums)
        # if freq(m) < k in window  -> expand window to right
        # else -> shrink window from left until subarray has freq(m)< k-1. 
        #         every window that was shrunken down had freq(m)>=k,
    
        result = 0
        m = max(nums)
        freq_m = 0 # count of m in current window
        left, right = 0,0 # sliding window start/end
        
        while right<len(nums):
            
            if nums[right] == m:
                freq_m += 1
                
            # shrink from left until remove leftmost m
            # each iteration of this represents a satisfactory subarray
            while freq_m == k: 
                if nums[left] == m:
                    freq_m -=1
                left +=1
                
            result += left # each subarray nums[:left-1] and nums[left:right+1] satisfies freq(m)>=k
            right+=1
        
        return result