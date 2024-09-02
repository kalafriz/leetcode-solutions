class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        k = (int) (k % sum(chalk))
        i=0
        
        while k>=chalk[i]:
            k -= chalk[i]
            i += 1
            
        return i