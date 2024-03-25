class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        n = len(nums)
        found = [0]*n
        twice = []
        for x in nums:
            found[x-1] +=1
            if found[x-1]==2:
                twice.append(x)
        return twice