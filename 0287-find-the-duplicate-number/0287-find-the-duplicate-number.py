class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)-1
        found = [0]*n
        for x in nums:
            if found[x-1]==1:
                return x
            found[x-1] = 1
        return 0