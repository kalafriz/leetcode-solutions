class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        
        # METHOD: sliding window
        #
        # To find # subarrays with AT MOST k unique ints:
            # let u = # of unique ints in current window subarray
            # if u<k -> expand to right
            # if u>k -> shrink from left unitl u==k
            # if u==k -> # good subarrays is len(window)+1
        #
        # To find # subarrays with EXACTLY k unique ints:
        # (# with at most k) - (# with at most k-1)
        
        return self.subarraysWithLEQKDistinct(nums, k) - self.subarraysWithLEQKDistinct(nums, k-1)
        
    def subarraysWithLEQKDistinct(self, nums:List[int], k:int) -> int:
        
        
        if nums == []:
            return 0
        
        result = 0
        count = [0]*(max(nums)+1) #faster than 'in'
        unique = 0
        left,right = 0,0
        
        while right<len(nums):
            count[nums[right]] +=1
            if count[nums[right]]==1:
                unique +=1
                
            #print(nums[left:right+1], ", u=",unique)
            
            while unique > k:
                #print("shrinking: ",nums[left:right+1])
                count[nums[left]] -=1
                if count[nums[left]]==0:
                    unique -=1 
                left +=1 
                
            #print("result = ", result,"+",right-left+1)
            result += right-left+1
            right +=1
        
        return result