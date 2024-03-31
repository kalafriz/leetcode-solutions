class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        
        # METHOD: sliding window
        # let m = max(nums)
        # if minK or maxK not in window  -> expand window to right
        # 
        # if minK and maxK in window
        # AND rightmost not in fixed-bound -> 
        #        Restart with an empty window [] the next element over
        # else -> expand to right
        #
        # if window is fixed-bound -> 
        #       A new satisfactory subarray is made by selecting from rightmost until
        #       one of minK and maxK are included. Then, expand this all the way to
        #       leftmost of window. This amount is min(lastMin, lastMax)+1 - left
    
        result = 0
        minCount, maxCount = 0,0 # use as both count and boolean for has min/max
        left, right = 0,0 # sliding window start/end
        lastMin, lastMax = 0,0
        
        while right<len(nums):
            
            if nums[right]==minK:
                minCount += 1
                lastMin=right
            if nums[right]==maxK:
                maxCount += 1
                lastMax=right
            
            #print(nums[left:right+1], ", minCount:", minCount, ", maxCount:", maxCount)
            
            if nums[right] < minK or nums[right]>maxK:
                #print(nums[right]," out of bounds.")
                left=right+1
                right=left
                minCount, maxCount= 0,0
            else:
                right +=1
        
            if minCount>0 and maxCount>0:
                result += min(lastMin, lastMax)+1 - left
                #print("result: ",result)
            
        return result