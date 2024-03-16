class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        
        sublen_map = {0: -1} 
        max_sublen = 0
        count = 0
        
        for i, n in enumerate(nums):
            count +=1 if n==1 else -1
            
            if count in sublen_map:
                current_count = i-sublen_map[count]
                max_sublen = max(max_sublen, current_count)
            else:
                sublen_map[count]=i
        
        return max_sublen
            
        