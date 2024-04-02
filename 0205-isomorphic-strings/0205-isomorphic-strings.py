from collections import defaultdict
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        # METHOD:
        # Iterate through strings, mapping chars next to each other as
        # you go. If find already mapped char to a mismatch, return false.
        
        charMap = {}
        
        for i, c in enumerate(s):
            #print(c, t[i])
            
            if (c not in charMap):
                if t[i] in charMap.values() :
                    return False 
                else:
                    charMap[c] = t[i]  
    
            if charMap[c] != t[i]:
                return False
                
        return True