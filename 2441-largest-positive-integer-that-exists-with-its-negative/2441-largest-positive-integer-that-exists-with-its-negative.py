class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        
        # METHOD: two pointer
        
        nums.sort()
        #print(nums)
        i, j = 0, (len(nums)-1)
        
        while i<j and nums[i]<0 and nums[j]>0:
            
            x, y = abs(nums[i]), nums[j]
            #print(-1*x, y)
            
            if x == y:
                return y
            elif x < y: # pick a smaller + number
                j-=1
            else: # x > y, pick a larger - number
                i+=1
        return -1