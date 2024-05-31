class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        frequency_map = {}
        
        # Build the frequency map
        for num in nums:
            frequency_map[num] = frequency_map.get(num, 0) + 1
        
        # Find the elements that appear only once
        result = [num for num, count in frequency_map.items() if count == 1]
        
        return result