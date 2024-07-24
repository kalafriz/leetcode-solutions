class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        mapped = []
        for i, x in enumerate(nums):
            y = ''
            for d in map(int, str(x)): # for digit in x
                y += str(mapping[int(d)])
            y = int(y.lstrip('0')) if y.lstrip('0') else 0 # convert to int, remove leading 0's
            mapped.append(y)
        
        nums = [x for _, x in sorted(zip(mapped, nums), key = lambda pair: pair[0])]
        return nums