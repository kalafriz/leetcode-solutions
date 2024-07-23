from collections import defaultdict

class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        nums.sort(reverse=True)
        freqDict = defaultdict(int)
        
        for x in nums:
            freqDict[x] += 1
        
        nums.sort(key = lambda x: freqDict[x])
        return nums