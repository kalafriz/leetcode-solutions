class Solution:
    def numSteps(self, s: str) -> int:
        
        ops, carry = 0, 0
        
        for x in s[:0:-1]:
            val = int(x) + carry
            if val%2 == 1:
                ops +=2
                carry = 1
            else:
                ops +=1
                
        return ops + carry