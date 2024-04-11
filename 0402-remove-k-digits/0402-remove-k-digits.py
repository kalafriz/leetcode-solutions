class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        
        # METHOD: Greedy stack
        # Goal: minimize the high-value digits
        
        # While k>0, minimize the leftmost digit.
        # Iterate L->R through digits of num.
        # If selected digit is greater than current digit,
        # AKA there is an opportunity to decrease left digit,
        #   select the current digit and discard the formerly selected (decrease k by 1)
        # Otherwise, move on to selecting the next leftmost digit.
        
        stack = []
        i = 0
        
        for x in num:
            
            while k > 0 and (stack and stack[-1] > x):
                stack.pop()
                k-=1
            
            stack.append(x)
            #print(k, stack)
        
        # If we didn't need to keep minimizing, remove last digits 
        #   (selecting these would not have minimize the result)
        if k > 0:
            stack = stack[:-k]
        
        #print(k, stack)
        
        # Convert stack to string and remove leading 0's

        result = "".join(stack).lstrip("0")
        result = "0" if result=="" else result
        
        return result
    