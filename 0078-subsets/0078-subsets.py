class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        return powerset(nums)
    
def powerset(s):
    n = len(s)
    masks = [1 << i for i in range(n)]
    for i in range(1 << n):
        yield [ss for mask, ss in zip(masks, s) if i & mask]