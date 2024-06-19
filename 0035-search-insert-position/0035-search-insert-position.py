class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        left, right = 0, len(nums)-1
        mid = (left + right)//2
        
        while left<=right:
            
            mid = (left + right)//2
            
            if nums[mid]==target:
                return mid
            if nums[mid]<target:
                left = mid+1
            else: #nums[mid]>target
                right = mid-1
        
        return mid+1 if target>nums[mid] else mid