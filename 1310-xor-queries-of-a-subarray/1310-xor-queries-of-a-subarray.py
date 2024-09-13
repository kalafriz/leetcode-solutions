class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        
        answer = []
        
        # Convert arr into prefix XOR arr
        for i in range(1, len(arr)):
            arr[i] ^= arr[i-1]
        
        
        # Use prefix XOR arr for each query
        # (left) XOR (left+1) XOR ... XOR (right)
        #    = 
        # (left-1 prefix XOR) XOR (right prefix XOR)
        for left, right in queries:
            if left > 0:
                answer.append(arr[left-1] ^ arr[right])
            else:
                answer.append(arr[right])
                
        return answer