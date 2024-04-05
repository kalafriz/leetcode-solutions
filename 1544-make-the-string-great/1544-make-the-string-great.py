class Solution:
    def makeGood(self, s: str) -> str:
        if s=="":
            return s
        
        for i in range(len(s)-1):
            
            #print(s, s[i], ord(s[i]), s[i+1], ord(s[i+1]), ord(s[i])-ord(s[i+1]))
            if abs(ord(s[i])-ord(s[i+1])) ==32:
                
                if i >= len(s)-1:
                    return self.makeGood(s)
                else:
                    return self.makeGood(s[:i]+s[i+2:])
        
        return s