class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        
        # METHOD:
        # sort copy of arr - O(n)
        # make hash table of number:rank from sorted copy (faster than indexOf()) - O(n)
        # replace each element of arr with hashed rank
        
        if not arr:
            return[]
        
        sortedArr = arr.copy()
        sortedArr.sort()
        print(arr, sortedArr)
        rank = 1
        rankDict = defaultdict(int)
        rankDict[sortedArr[0]] = rank
        
        for i in range(1, len(sortedArr)):
            # if not same as previous, increase rank
            if sortedArr[i] != sortedArr[i-1]:
                rank += 1
                rankDict[sortedArr[i]] = rank
            # else if same as previous, rank will not increase, and will already be in dict
        
        for i,n in enumerate(arr):
            arr[i] = rankDict[n]
            
        return arr