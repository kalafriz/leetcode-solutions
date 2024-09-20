class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if s == "":
            return s
        
        left = 0
        
        for right in range(len(s)-1, -1, -1):
            if s[right] == s[left]:
                left += 1
            
        if left==len(s):
            return s
        
        # Extract the suffix that is not part of the palindromic prefix
        non_palindrome_suffix = s[left:]
        reverse_suffix = non_palindrome_suffix[::-1]

        # Form the shortest palindrome by prepending the reversed suffix
        return (
            reverse_suffix
            + self.shortestPalindrome(s[:left])
            + non_palindrome_suffix
        )
        