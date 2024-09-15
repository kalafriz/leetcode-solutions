class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        
        # METHOD: Prefix XOR
        
        # Store bools for each vowel as bitmask of length 5 (i.e. 00000)
        
        # Take the prefix XOR for each char in the string:
        #    if char is a vowel, flip its val in the bitmask
        
        # If a prefix XOR of the current char has occurred at a prev char,
        #   then the substring between them contains even vowels
        
        # Assign bit values to each char for calculating prefix XOR
        charmap = [0]*26
        charmap[0], charmap[ord('e')-ord('a')], charmap[ord('i')-ord('a')], charmap[ord('o')-ord('a')], charmap[ord('u')-ord('a')],= 1, 2, 4, 8, 16
        
        # Keep track of first occurence of each possible prefix XOR value
        # 00000 -> 11111 is 32 combinations
        firstOccurrence = [-1] * 32
        
        prefixXOR = 0
        
        result = 0 # longest substring length
        
        # Calculate prefix XOR and update result
        for i, c in enumerate(s):
            prefixXOR ^= charmap[ord(c)-ord('a')]
            
            # update first occurrence array if applicable
                # don't include 0 so we start from beginning of string
            if firstOccurrence[prefixXOR] == -1 and prefixXOR != 0:
                firstOccurrence[prefixXOR] = i
            
            # update result
            result = max(result, i-firstOccurrence[prefixXOR])
        
        return result