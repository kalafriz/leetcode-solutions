class Solution:
    def minSteps(self, n: int) -> int:
        # METHOD: prime factorization
        # break down n into prime factors, 
        # then calc min moves 
        
        moves = 0
        i = 2 # prime factor
        
        while n > 1:
            while n % i == 0:
                n = n//i
                moves += i # first move copies, rest of them paste
                           # i.e. 'AA' with i=3: 1. copy all, 2. paste all, 3. paste all -> 'AAAAAA', len=6 
                
            i+=1 # increment to next prime factor
                 # note: since we already divide at thier prime factorizations,
                 #       the loop will just skip for non-prime numbers
            
        return moves