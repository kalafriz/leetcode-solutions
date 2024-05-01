class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        end = word.find(ch)
        if end > -1:
            return word[end::-1]+word[end+1:]
        else:
            return word