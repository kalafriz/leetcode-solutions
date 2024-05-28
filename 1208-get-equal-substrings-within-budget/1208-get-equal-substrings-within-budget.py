class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
         
            # METHOD: Sliding Window
            cost = 0
            start = 0
            maxLen = 0
            
            for i, x in enumerate(s):
                y = t[i]
                
                cost += abs(ord(x)-ord(y))
                
                # While over cost -> slide start of window to right
                while cost > maxCost:
                    cost -= abs(ord(s[start])-ord(t[start]))
                    start +=1
                
                maxLen = max(maxLen, i-start+1)
                
            return maxLen