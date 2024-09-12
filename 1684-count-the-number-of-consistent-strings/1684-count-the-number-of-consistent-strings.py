class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        
        # Bitmask of chars in allowed
        allowedMask = 0
        
        # For each character in allowed,
        # Set the bit at its corresponding position 
        #    - position is bit at difference in ord between character and a
        # And set it to 1
        #    - Do so by bitshifting 1 so that it will be in target char bit position,
        #       then OR operation w current allowed bit mask
        for c in allowed:
            allowedMask |= 1 << (ord(c) - ord('a')) 
        
        result = 0 # count of consistent strings in words
        
        for word in words:
            
            isConsistent = True
            
            for c in word:
                
                # check if bit position in allowed mask corresponding to c is 1
                #   if not, this word is not consistent
                if not (allowedMask >> (ord(c)-ord('a'))) & 1:
                    isConsistent = False
                    break
            
            if isConsistent:
                result +=1
        
        return result