class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        # If and only if between the two sentences a word appears once,
        # then it is uncommon
        
        words = s1.split()+s2.split()
        wordFreq = defaultdict(int)
        
        for w in words:
            wordFreq[w] += 1
            
        result = []
        
        for w in wordFreq:
            if wordFreq[w] == 1:
                result.append(w)
        
        return result