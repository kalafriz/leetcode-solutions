class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        
        # XOR returns 1 where different (flip is necessary), 0 where same
        xorResult = start ^ goal
        numOnes = 0
        
        # Count how many bits differed by counting how many 1's
        while xorResult:
            
            # Detect if rightmost bit is 1:
            # Do AND operation with result and 1 (AKA ....00001).
            # This will be 0 for all preceeding bits,
            # and just compare the rightmost with 1
            numOnes += xorResult & 1
            
            # Go to next bit by shifting to right
            xorResult >>=1
        
        return numOnes