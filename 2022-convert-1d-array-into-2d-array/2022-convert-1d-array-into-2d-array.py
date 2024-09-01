class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        
        result = []
        if len(original) != (m*n):
            return result
        
        i=0
        while i < len(original):
            result.append(original[i:i+n])
            i+=n
        
        return result